# Race Conditions

[Race Conditions](https://tryhackme.com/room/raceconditions)

## Solution

### Walk

The trick here is that path check does not check if the file actually exists,
it only checks if the name is equal to `flag`.

```c
int path_check = strstr(argv[1], "flag");
```

this returns `NULL` when there is no match.

The code then checks if the given file is a symlink, but again it does not
check if the file exists.

```c
lstat(argv[1], &lstat_buf);
int symlink_check = (S_ISLNK(lstat_buf.st_mode));
```

Basically `lstat` will fail with `ENOENT` and `S_ISLNK` will return `0`. This
happens because there are no error checks for `lstat`.

To get the program to print the flag we have to create a symlink to the flag
file while the program runs.

Start the program with an argument as the path of the file to print (we will
create this file as a symlink)

```console
./anti_flag_reader ../race/file
```

this will start the reader process and it will wait for an input from the user

In another terminal create the symlink

```console
ln -s ../walk/flag file
```

then press Enter in the other terminal and it should display the flag.

### Run

In this one, the coder makes a check to see if the user has read permissions on the given file

```c
context_result = access(file_name, R_OK);
```

but then there is a small window in which we can do some mallicious activity

```c
usleep(500);
```

The idea in this case is also to use symlinks, but we now have to run the two processes in parallel.

First we will create a file that we have read access to, for example using touch.

```console
touch file
```

then we can run the exploit

```console
./cat2 /home/race/file & ln -sf /home/run/flag /home/race/file;
```

This will execute the two prcesses in parallel, and the `ln -f` will overwrite
the old file with a symlink to the flag, hopefully after the check using
`access` is performed.

### Sprint

This one felt easier to figure out than the others (I am speaking about the
bash code to exploit it). The source code was pretty easy to follow too.

Basically we have a server that starts a new thread for each connection. Then
in the thread function it checks for what you have sent in the payload. If you
sent `deposit` it will add 10000 to the money variable, etc.

The issue is that the thread function resets the money variable to 0 at the
end. However, this is not protected by a mutex, so if we spawn another thread
quick enough, we might have the money variable at a value other than 0.

For example, if we do `deposit` 2 times in parallel, we might end up with 20000
money and we should be able to get the flag. So the shell code looks like

```console
(echo deposit | nc $IP 1337) & (echo deposit | nc $IP 1337) & (echo "purchase flag" | nc $IP 1337)
```

However this doesn't work everytime. You have to get lucky and the "purchase
flag" to be sent last. I guess you can write this also in Python and do it with
threads or something, start a connection on 3 threads and when they all connect
send the payload in order.
