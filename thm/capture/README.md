# Capture

[Capture](https://tryhackme.com/room/capture)

## Solution

- nmap scan: 80

Python script

Iterate all the usernames and check if the server responds with "The user ...",
which would mean that the username is not correct. If the server has another
response it means we gucci. Then do the same for passwords and check for
"Invalid password".

After a couple of wrong attempts we need to solve a captcha. Which we can do
with just `eval`, we search for `?` which will be unique, split by `=` and take
the left hand side and run it trough `eval`.

Finally we are left with the username and password. If we log in we get the flag.
