# Cat Pictures 2

[TryHackMe Room](https://tryhackme.com/room/catpictures2)

## Solution

- setup the VM `export IP=...`

- nmap scan `nmap -sC -sV $IP`: 22, 80, 222, 3000, 8080

### Explore options

- port 80:
    - we find a Self-hosted photo-management website using Lychee. Nothing unusual.
    - the first cat image contains a description: `note to self: strip metadata`.
    - download the image from `http://$IP/uploads/big/f5054e97620f168c7b5088c85ab1d6e4.jpg`
    - if we run `exiftool` on the image we find a `Title` section with the value `:8080/764efa883dda1e11db47671c4a3bbd9e.txt`

- port 8080:
    - we can try to access the path from the cat image
    - on the given page we find a password for the `samarium` user for a gitea service.
    - we also find that ansible is running on port 1337

- port 3000:
    - we find a Self-hosted git service using gitea. If we look around we find an user `samarium`.
    - we also see that the version used is `Powered by Gitea Version: 1.17.3`
    - at this point we can try to use the password that we found in the previous step.

- ansible:
    - we have to access the commit with the title `add flag` and look at the flag.txt file
      `http://$IP:3000/samarium/ansible/raw/commit/8be5b40d15cfdfd8996e1bb13bdf416eb249bdb0/flag.txt`
      but actually the flag1.txt file has the same content.
      `http://$IP:3000/samarium/ansible/raw/branch/main/flag1.txt`
    - I have found an user `bismuth` that might be running on the server

- port 1337:
    - we can run the playbook.yaml file from here
    - so we have to change the code from the repo to use a revshell from <https://www.revshells.com/>
    - we find the second flag in the home directory of bismuth

- on the machine:
    - we can use the `.ssh/id_rsa` key to connect with ssh to avoid using the revshell
    - use linpeas.sh
    - we find that we have a vulnerable sudo version
    - one video I saw on the topic (from two years ago :O) https://www.youtube.com/watch?v=TLa2VqcGGEQ
    - we can use https://github.com/teamtopkarl/CVE-2021-3156/tree/main
    - I have cloned the repo, then started a http server and send each file to the target
    - then I ran make and `./sudo-hax-me-a-sandwich 0`
    - we then get root access and can show the flag from the root home
