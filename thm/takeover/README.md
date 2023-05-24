# TakeOver

[TakeOver](https://tryhackme.com/room/takeover)

## Solution

```bash
export IP=...
echo "$IP secrethelpdesk934752.support.futurevera.thm" | sudo tee -a /etc/hosts > /dev/null
curl -s -I http://secrethelpdesk934752.support.futurevera.thm | sed -n '4p' | grep -o 'flag{.*}'
sudo sed -i '$d' /etc/hosts
```

or just run

```bash
./solve.sh $IP
```
