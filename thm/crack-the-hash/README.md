# Crack the hash

[Crack the hash](https://tryhackme.com/room/crackthehash)

## Solution

### Task1

I used john for

1. `48bb6e862e54f2a795ffc4e541caed4d` raw-md5

2. `CBFDAC6008F9CAB4083784CBD1874F76618D2A97` raw-sha1

3. `1C8BFE8F801D79745C4631D09FFF36C82AA37FC4CCE4FC946683D7B336B63032` raw-sha256

4. `$2y$12$Dwt1BZj6pcyc3Dy1FWZ5ieeUznr71EeNkJkUlypTsgbX1H68wsRom` bcrypt (slow... use some sort of mask for 4 characters)

5. `279412f945939ba78ce0758d3fd83daa` raw-md4

### Task2

1. `F09EDCB1FCEFC6DFB23DC3505A882655FF77375ED8AA2D1C13F640FCCC2D0C85` sha256

2. `1DFECA0C002AE40B8619ECF94819CC1B` NTLM

3. `$6$aReallyHardSalt$6WKUTqzq.UQQmrm0p/T7MPpMbGNnzXPMAXi4bJMl9be.cfi3/qxIf.hsGpS41BqMhSrHVXgMpdjS6xeKZAs02.` sha512crypt

4. `e5d8870e5bdd26602cab8dbe07a942c8669e56d6:tryhackme` HMAC-SHA1
