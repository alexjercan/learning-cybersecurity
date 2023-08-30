# Grep

[TryHackMe Room](https://tryhackme.com/room/greprtp)

## Solution

nmap scan: 22, 80, 443, 51337

port 443 forbidden

add grep.thm to /etc/hosts

access <https://grep.thm/public/html/>

the api key from <https://grep.thm/public/js/register.js> is not correct

osint: search on github for `Welcome to SearchME!` and found one repo <https://github.com/supersecuredeveloper/searchmecms>

in the repo the key was removed at some point: <https://github.com/supersecuredeveloper/searchmecms/commit/db11421db2324ed0991c36493a725bf7db9bdcf6>

can change the source from the browser console to the new API key and create a new account

we find the first flag on the dashboard page

the upload page <https://grep.thm/public/html/upload.php> inside the repo there is a upload.php file which checks the magic bytes of the file

I found this repo <https://github.com/S12cybersecurity/bypass_magic_bytes> which creates a png image with a payload that executes a command

Create a png image with `./magic_bytes.sh` then upload the image and then access <https://grep.thm/api/uploads/mime_shell.php?cmd=id> where you can provide any command to cmd

Next we can run a revshell from <https://www.revshells.com/> I used `PHP exec` with URL encoding and passed the string to the cmd argument

Inside of /var/www are some useful files

1. The backup folder with the `users.sql` file which contains the admin email (and the password hash)
2. The leakchecker folder which container some scripts
3. leak certificates `openssl x509 -in leak_certificate.crt -text -noout` where we find the domain name of the leak service

We can add the hostname in /etc/hosts and try to see what the service is about. I randomly entered the admin email and it gave the password
