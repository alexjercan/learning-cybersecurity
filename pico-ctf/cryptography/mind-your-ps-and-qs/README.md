# Mind your Ps and Qs

[Mind your Ps and Qs](https://play.picoctf.org/practice/challenge/162)

## Description

In RSA, a small `e` value can be problematic, but what about `N`? Can you decrypt this? values

## Solution

My [RSA](https://github.com/alexjercan/haskell-rsa) implementation can be helpful.

We have the `n` and `e` values so we can compute the `d` value to perform
decyrption on the `c` value. First we have to factor the `n` into primes
`p` and `q`. I did this using a tool called `alpertron`. Then I computed the
`lambda_n` value as `(p-1) * (q-1)` and then the `d` value as the mod inverse of
`e` and `lambda_n`, knowing that `e * d mod lambda_n == 1`. Then to compute the
decrypt `c` value we can compute `c ** d mod n`.
