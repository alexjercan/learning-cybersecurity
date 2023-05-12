# Cyborg

[Cyborg](https://tryhackme.com/room/cyborgt8)

## Solution

- nmap scan 22, 80

1. Scan the machine, how many ports are open?

we can run `nmap <ip>` and get the answer `2`.

2. What service is running on port 22?

we can use `nmap -sV -p 22 <ip>` and get the answer `ssh`.

3. What service is running on port 80?

we can use `nmap -sV -p 22 <ip>` and get the answer `http`.

4. What is the user.txt flag?

we can use feroxbuster to enumerate the directories that we can access.

we find an interesting folder `/etc/squid`. there is a file `passwd` which
contains a an encrypted MD5(APR) string. we can crack it with `hashcat -m 1600
'$apr1$BpZ.Q.1m$F0qqPwHSOG50URuOVQTTn.' /path/to/wordlist`. and we get
`squidward`. so we have what looks like a username password
`music_archive:squidward`. we can try ssh, but we get permission denied.

another interesting directory is `/admin`. here we can find some intel that the
person who owns the site is called `alex` and he is noob in security. `im
pretty sure my backup "music_archive" is safe` this statement is SUS. from here
we can get a tar archive. and we can decompress it using `tar -xf archive.tar`.

inside it is a borg backup archive. we can run `borg extract
/home/field/dev/final_archive::music_archive` and provide `squidward` as the
password. the password file might have beed for this thing.

now we seemingly have alex's entire home directory so we can view interesting
files like `cat home/alex/Documents/note.txt` which contains his password
`alex:S3cretP@s3` now we can actually try ssh `ssh alex@<ip>` and we give the
password. you can read the flag using `cat ~/user.txt`.

5. What is the root.txt flag?

we can try to see if we have sudo privilage with `sudo -l` and we can see that
we can run `(ALL : ALL) NOPASSWD: /etc/mp3backups/backup.sh`. if we cat that
file we can see that it takes an argument with `-c` and at the end it just
evaluates it. so we can pass `/bin/bash` and spawn a root shell. and then get
the flag from root. we just need to make this fancier and redirect stdin and
stdout. one way is to just suid the /bin/bash binary and execute it.
nonetheless the flag is in /root/root.txt.

funny enough if we press up arrow in alex's shell we get the answers...

