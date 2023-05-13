# Internal

[Internal](https://tryhackme.com/room/internal)

## Solution

### Initial enumeration

- nmap scan; open ports 22, 80
- feroxbuster; /blog Scanning with feroxbuster this looks like a wordpress blog.

### Wordpress

wpscan https://github.com/wpscanteam/wpscan

enumerate users with `wpscan --url  http://internal.thm/blog --enumerate u` and
we find `admin`. we can bruteforce passwords using `wpscan --url
http://internal.thm/blog -U admin -P /path/to/rockyou.txt`.

we get the username and password: `admin:my2boys`.

### Revshell

now we go to `Appearance` -> `Theme Editor` -> `404 Template` and we can change
it to a revshell https://www.revshells.com/

then we start a nc listener `nc -lvnp 6969` and navigate to
http://internal.thm/blog/wp-content/themes/twentyseventeen/404.php

now we should have a shell open as www-data

### User

Enumerate:
- search for config in `/var/www/html/wordpress`, we can `cat *.php` and search
  for password, something interesting MySQL creds `wordpress:wordpress123`,
  however we cannot find anything useful in the database.
- look into directories that we have permissions to read/write etc. one location could be `/opt`.

we can find the credentials for the user in `/opt/wp-save.txt`
`aubreanna:bubb13guM!@#123` so next we can ssh into that user.

we find the flag in `~/user.txt`.

### Root

Enumerate:
- `sudo -l`: nothing
- `find / -type f -perm -4000 2> /dev/null`: nothing interesting
- `cat ~/jenkins.txt`: `Internal Jenkins service is running on 172.17.0.2:8080`
- `crontab -l`: nothing

 we can create a ssh tunnel to redirect trafic from `localhost:8080` to the
 internal `172.17.0.2:8080` using: `ssh -L 8080:172.17.0.2:8080 aubreanna@<ip>`
 (man ssh)

we can try a random login attempt and look at the network tab the data sent to
the server looks like this:

```
j_username: admin
j_password: password
from: /
Submit: Sign in
```

this means we have to use `j_username=^USER^&j_password=^PASS^&from=%2F&Submit=Sign+in`.
the path is also in the network. we made a POST request to `/j_acegi_security_check`.
and the error message that appears is "Invalid username or password".

this means the string will be `"/j_acegi_security_check:j_username=^USER^&j_password=^PASS^&from=%2F&Submit=Sign+in:F=Invalid username or password"`

then we can try to use hydra to get inside the jenkins website.

```console
hydra -f -V -l admin -P /usr/share/wordlists/rockyou.txt localhost -s 8080 http-post-form "/j_acegi_security_check:j_username=^USER^&j_password=^PASS^&from=%2F&Submit=Sign+in:F=Invalid username or password"
```

I cannot get this thing to work tho... idk why. so I tried to instead of using
:F=... to use `:S=Dashboard`, check for success instead of failure. and we get
`spongebob`. man this took me like 2 hours.

after we login with `admin:spongebob` we can go to `Manage Jenkins` -> `Script
Console` and we can run a Groovy revshell from https://www.revshells.com/ (make
sure to have a nc listener ready).

again the credentials are stored in `/opt/note.txt` root:tr0ub13guM!@#123

then we can go to the ssh machine and `su root` with this new password. the
flag is in /root/root.txt
