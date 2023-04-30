# Mr Robot CTF

[Mr Robot CTF](https://tryhackme.com/room/mrrobot)

## Solution

- `nmap -sS -sC -sV <ip>`

PORT    STATE  SERVICE  VERSION
22/tcp  closed ssh
80/tcp  open   http     Apache httpd
|_http-title: Site doesn't have a title (text/html).
|_http-server-header: Apache
443/tcp open   ssl/http Apache httpd
|_http-title: Site doesn't have a title (text/html).
| ssl-cert: Subject: commonName=www.example.com
| Not valid before: 2015-09-16T10:45:03
|_Not valid after:  2025-09-13T10:45:03
|_http-server-header: Apache

- `dirsearch -u <ip>` - doesn't seem like it works

- `dirb <ip>` - works better I guess

- the website is like a terminal with some command options. first I might play
  around with it as intended; try to find some edge cases or something like
  that. maybe the point is to somehow get ssh access. maybe try with the
  email... I mean I don't see any other interesting thing.

- randomly tried `robots.txt`

User-agent: *
fsocity.dic
key-1-of-3.txt

- accessing `key-1-of-3.txt` we get the first key.

- fsocity.dic looks like a word list; maybe we can use it for guessing stuff?
  `wget fsocity.dic`

- if we go to random url we can see that this is wordpress. is there anything
  useful about wordpress?

- dirb found an interesting directory `license` there is a base64 string at the
  bottom so maybe try to `echo "" | base64 -d` it. and this gives an username
  and a password. maybe try to use it on wordpress.

- we can connect on wordpress. looking around we can see the version we are
  using `4.3.1`. maybe there is some vulnerability on this version. This
  version is vulnerable to XSS. We can create a post with "<script>alert('XSS
  attack!');</script>" and it will display the alert box.

- but I found that wordpress is also vuln to revshell.
  https://www.hackingarticles.in/wordpress-reverse-shell/ we can script kiddie
  our way in like in the tutorial.

- we should also stabilize the shell using `python -c 'import
  pty;pty.spawn("/bin/bash")'`

- we are logged in as the daemon user. We can access an encrypted file from the
  robot home. `cat /home/robot/password.raw-md5`. Maybe we can use john. we can
  use `~/.local/share/john/run/john --format=raw-md5 password.raw-md5` on the
  file that contains the hashed password. it gives us the password. we can try
  to login as robot now. we cat the key-2-of-3.txt and get the second key. (the
  password is abcdefghijklmnopqrstuvwxyz)

- next we need to privesc. this time there is no `sudo -l` cheecky easy. so I
  found a command that searches all files that have SUID bit set `find / -perm
  -u=s -type f 2>/dev/null`. also the hint says `nmap` so it might be something
  related to that.

- you can execute nmap with the `--interactive` flag and spawn a shell with
  `!sh`. the shell with use the root user, so you can go in the root home and
  cat the last flag.
