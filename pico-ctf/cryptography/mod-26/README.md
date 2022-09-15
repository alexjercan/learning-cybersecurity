# Mod 26

[Mod 26](https://play.picoctf.org/practice/challenge/144)

## Description

Cryptography can be easy, do you know what ROT13 is? `cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_GYpXOHqX}`

## Solution

ROT13 is a cypher used for alphabetic characters. To solve the challenge you have to add `13` to each letter and then modulo `26` to get back a character between `a` and `z` (or `A` and `Z`), and to keep the numbers and special characters unchanged.