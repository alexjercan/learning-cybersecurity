#!/usr/bin/env python3

c = 240986837130071017759137533082982207147971245672412893755780400885108149004760496
n = 831416828080417866340504968188990032810316193533653516022175784399720141076262857
e = 65537

# Factor n into primes using alpertron
p = 1593021310640923782355996681284584012117
q = 521911930824021492581321351826927897005221

# Compute lambda(n)
lambda_n = (p - 1) * (q - 1)

# Compute d using mod inverse
d = pow(e, -1, lambda_n)

# Do decryption on c
a = pow(c, d, n)

# We can decode a as a hexadecimal number
print(bytes.fromhex(hex(a)[2:]).decode("utf-8"))
