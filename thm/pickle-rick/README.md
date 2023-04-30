# Pickle Rick

[Pickle Rick](https://tryhackme.com/room/picklerick)

## Solution

- `nmap -sS -sC -sV <ip>`

22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.6 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   2048 8d:19:c2:72:86:e9:0d:94:8f:46:df:c0:7c:fb:fa:95 (RSA)
|   256 88:21:49:49:af:14:eb:cb:55:2b:b1:7a:19:28:72:7a (ECDSA)
|_  256 d8:b2:f0:15:5d:89:5d:af:28:ac:19:b2:f1:f5:3c:be (ED25519)
80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Rick is sup4r cool
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

- try the website (port 80 is open) seems to be a simple static page. we can
  look into the source. there is a comment `Username: R1ckRul3s` with the
  username.

- rickandmorty.jpeg; maybe stego but I couldn't find anything interesting with
  simple tools.

- maybe try `dirsearch -u <ip>` and we get:
    - assets
    - login.php
    - robots.txt

- in assets I found some gifs and a new jpg image with a portal. Maybe that
  image has something inside. But it doesn't seem like it.

- robots.txt has a string inside `Wubbalubbadubdub`. Maybe that is the password.

- that combination worked. now we are greeted with something that runs bash
  command? but not all commands work. we can try a revshell maybe.

- we can run `php` from the command box. maybe we can have a php revshell thing.

- weird it doesn't work... maybe php to cat a file. and this works. we can use
  `php -r 'echo file_get_contents("filename.txt");'` instead of `cat`.

- we can display the first ingredient from the current directory. the hint
  suggests to search in other folders aswell. so I moved around and found the
  rick home directory with the second ingredient.

- now it looks like a dead end because the other folders are too large. and we
  cannot access folders like root. so just tried to run `sudo ls /root` and it
  worked without a password. it seems like we have sudo access without password.
  so we can see the final ingredient in the root home directory, and use the
  same method to print the contents.
