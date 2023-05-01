# Bounty Hacker

[Bounty Hacker](https://tryhackme.com/room/cowboyhacker)

## Solution

- nmap scan: 21, 22, 80
- dirb: not interesting

- however we can connect using anonymous on ftp.
- on the target machine we find 2 files. tasks.txt and locks.txt.
- in tasks we can see a username "lin", which we can try to ssh into.
- locks.txt looks like passwords, so we use it as wordlist.

`hydra -l lin -P locks.txt ssh://10.10.193.219`

- the user.txt file is on the Desktop

- since we know lin's password we can try to use `sudo -l`
- it looks like we have access to `tar`
- so we can archive the root home `sudo tar -czvf root.tgz /root/`
- and then extract it `tar -xzvf root.tgz` and we get the flag.

