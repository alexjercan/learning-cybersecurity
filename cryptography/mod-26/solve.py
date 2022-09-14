#!/usr/bin/env python3


def rot13_char_decode(c):
    if c >= "a" and c <= "z":
        return chr((ord(c) - ord("a") + 13) % 26 + ord("a"))
    elif c >= "A" and c <= "Z":
        return chr((ord(c) - ord("A") + 13) % 26 + ord("A"))

    return c


def rot13_decode(s):
    return "".join(([rot13_char_decode(c) for c in s]))


if __name__ == "__main__":
    print(rot13_decode("cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_GYpXOHqX}"))
