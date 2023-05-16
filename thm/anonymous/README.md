# Anonymous

[Anonymous](https://tryhackme.com/room/anonymous)

## Solution

Start the machine and wait for the ip address to become available. You can test
that you can connect to the machine by doing a simple ping command `ping $IP`.

### Enumeration

To enumerate the machine we start with a simple nmap to check which ports are
open. Then we can use `-sV` and `-sC` to probe service verions and run default
scripts.

- nmap scan: 21, 22, 139, 445

We find 4 ports open 21 is for the ftp service, 22 is for ssh and 139 and 445
are for smb.

Q: Enumerate the machine. How many ports are open?
A: 4

Q: What service is running on port 21?
A: ftp

Q: What service is running on ports 139 and 445?
A: smb

We can further enumerte the ports and check for more information. But first, to
answer the next question we should take a look at the smb service. So we run
`smbclient -L $IP` to list the shares that are available. When you are propted
for a password just press Enter.

Besides the usual shares we observe a custom one called `pics`. So we can try
to connect to that share with `smbclient \\\\$IP\\pics` and we can download the
images with get.

Q: There's a share on the user's computer.  What's it called?
A: pics

### Anonymous FTP

Something else that we can do is try to anonymously connect to the ftp service,
by doing `ftp $IP` and providing the username `anonymous` and empty password.
In here we can see that there is a scripts folder that we can download to our
host using get.

Judging by the output that is present in the
`/var/ftp/scripts/removed_files.log` it seems like the
`/var/ftp/scripts/clean.sh` runs periodically. To validate this idea we can try
to modify the clean.sh script and the use `put` to upload it with ftp. I will
just change the string that is printed to the log file to something else and
then check the log file to see if it changes.

The log shows that the clean.sh scripts is indeed being executed using some
sort of a cronjob. This means that we can modify the clean.sh script with a
revshell payload to connect to the machine. You can try a bash revshell from
https://www.revshells.com/. I used the `nc mkfifo` one, and added that shell
line in the first branch of the if statement, just to be sure I do not modify
the script too much. I don't think it matters, but I tought it would be cool if
we try to blend in with the already existing stuff.

We start a nc listener `nc -lvnp 6969` and then we upload the new clean.sh
script to the ftp directory. After a bit of time it will connect and give you a
revshell. You can find the user flag in the user.txt file.

### namelessone

In the home directory of the namelessone user is a pics folder which is
familiar to us from the smb share with the same name.

We can also do some other basic enumeration, for example:
- check environment variables using the `env` command;
- check some common folders like `/opt` `/tmp` `/var` for interesting files;
- search for SUID binaries using `find / -type f -perm -4000 2> /dev/null`;
- if we check `crontab -l` we can actually see the cronjob for the `clean.sh` script;

Finally if we do not find anything useful manually we can also try to run
`linpeas.sh`. The script shows us that `env` is a potential privesc vector. We
know that it has the SUID bit set since we did some manual enumeration. So how
can we exploit this? We can check the man pages for env `man env` and we see:
"env - run a program in a modified environment". Funny enough this is a new for
me. I tought env was used only to show the environment variables, but it can
also be used to run commands. This means that we can run bash from env.

```
env bash -p
```

You can check what the `-p` flag does in the man for bash `man bash`.

Now we have a root shell so we can go to the home directory `/root` and print
the flag from `/root/root.txt`.
