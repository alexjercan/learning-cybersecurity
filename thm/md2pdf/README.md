# MD2PDF

[MD2PDF](https://tryhackme.com/room/)

## Solution

nmap scan: 22, 80, 5000
feroxbuster: $IP:5000/admin

```console
./exploit.py $IP
xdg-open ticket.pdf
```
