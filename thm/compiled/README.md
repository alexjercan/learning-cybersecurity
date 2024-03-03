# Compiled

[TryHackMe Room](https://tryhackme.com/room/compiled)

## Solution

- the binary is not stripped (it was compiled with -g)
- used radare2 to see the assembly code
- the password has `DoYouEven` prefix
- first we check if the string is larger than `__dso_handle` and if it is we
  compare with `_init` and if it equal to `_init` it is correct
- so the password was `DoYouEven_init`
