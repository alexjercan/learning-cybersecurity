# Obscure

[Obscure](https://tryhackme.com/room/obscured)

## Solution

- nmap scan: 21, 22, 80

### Part 1

We see from the nmap scan that we can connect using anonymous session with ftp.
In the fpt session we find a `notice.txt` file and an ELF executable called
`password`. From the notice `password` is an application that stores passwords?

Intresting `strings`:

```
SecurePaH
ssword12H
```

We can `chmox +x password` and try to run it. We get the following message:

```
Password Recovery
Please enter your employee id that is in your email
```

If we try to break  the app with a very long string we get `*** stack smashing
detected ***: terminated` so we might not be able to redirect code execution.
We can try to gdb into the executable and try to see if we can somehow exploit
the tool.

Using gdb we can see that the input is compared using strcmp with `971234596`,
which is one of the strings of the executable, and it seems that it is the user
id. We can try to run the executable with that value.

After runnin the `password` tool with the input `971234596` we get
`SecurePassword123!`. This might be useful later. Maybe there is something else
in the code that we can do.

We can access the website on port 80. After playing around a bit, I tried to go
to `Manage Databases`. There I tried to run backup and provided the password
that we got from the executable. And it downloaded a zip archive.

Scanning trought the `dump.sql` file I found something interesting `1	t
admin@antisoft.thm		1	3	\N	f	1	\N	\N	2022-07-23 10:52:10.087949
<span data-o-mail-quote="1">-- <br data-o-mail-quote="1">\nAdministrator</span>
$pbkdf2-sha512$12000$lBJiDGHMOcc4Zwwh5Dzn/A$x.EZ/PrEodzEJ5r4JfQo2KsMZLkLT97xWZ3LsMdgwMuK1Ue.YCzfElODfWEGUOc7yYBB4fMt87ph8Sy5tN4nag`

Funny enough, the login `admin@antisoft.thm` and password `SecurePassword123!`
works on the website. (We can try and see if hashcat finds the same password,
but it's not necessary).

I was randomly clicking on the sidebar (Apps, Updates) and got an error
`Uncaught TypeError: Cannot read properties of null (reading '0')`. Not sure if
it is relevant or not. There is also a `Settings` tab. Maybe that is more
interesting.

I searched for odoo on exploitdb and found something that looks promising. This
seems to match with the version that we have and is an actual thing. I spent so
much time on that. But it didn't work first try. I am too deep to not continue
on this rabbit hole. https://www.exploit-db.com/exploits/44064 There is another
button `Activate developer mode`... smh. Idk if that does something. Still no
idea what to do from here.

