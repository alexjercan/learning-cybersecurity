# Brooklyn Nine Nine

[Brooklyn Nine Nine](https://tryhackme.com/room/brooklynninenine)

## Solution

- nmap scan 21, 22, 80

- feroxbuster

### User

We can anonymously connect with ftp and check the contents. A single txt file.

```
From Amy,

Jake please change your password. It is too weak and holt will be mad if someone hacks into the nine nine
```

Maybe this will be useful if there is a `jake` user. He has a weak password.

Next we can check the website source. There is a comment.

```html
<!-- Have you ever heard of steganography? -->
```

We can try to download the image and check it for some clues. The basic tools
did not show anything (binwalk, exiftool, steghide) so move on.

I left feroxbuster to run in the backrgound, but it didn't find any directories.

Maybe next attempt is to try to crack jake's password using hydra.

```
hydra -l jake -P /usr/share/wordlists/rockyou.txt ssh://10.10.115.132
```

This worked. Jake has a very weak password. So next we can ssh into the box
using `jake:987654321`.

The flag for the first part is in the `holt` user directory.

### Root

We can check `sudo -l` since we know the password.

```
User jake may run the following commands on brookly_nine_nine:
    (ALL) NOPASSWD: /usr/bin/less
```

We can try to blind show the flag for root.

```
sudo /usr/bin/less /root/root.txt
```

And we get the flag.
