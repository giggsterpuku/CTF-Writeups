#!/usr/bin/env python3

################################### Write-Up ###################################
# Challenge: Dachshund Attacks
# Category: Crytography
# Description: What if d is too small? Connect with nc mercury.picoctf.net 31133.

# Hints:
#	-1: What do you think about my pet? dachshund.jpg
#
# The chall description and pic are hints to Weiner's attack, which is a
# cryptographic attack on RSA when the decrytion key d is smol. The process
# of the attack is basically automated in this script so you don't need to
# crank out the huge calculations, but the gist is that you can approximate
# d if d is less than the modulo (n ^(1/4)) / 3. The attack itself is
# focused on finding d by first finding continued functions and convergents
# of e/n and then solving for potential totients using the convergents
# and plugging them into a quadratic equation x^2 + (n - phi(n) + 1)x + n = 0
# and seeing if the roots of the equation are positive integers (p and q).
# From there, d can be found. After that, it's just standard RSA procedure:
# c^d mod n = m, and the plaintext can be found.
#
# Flag: picoCTF{proving_wiener_1146084}
# Points: 80
# Solved in picoGym
################################################################################

from Crypto.Util.number import *
from pwn import *
import owiener

r = remote("mercury.picoctf.net", 31133)
r.recvline()
e_str = r.recvline()[3:-1]
n_str = r.recvline()[3:-1]
c_str = r.recvline()[3:-1]
r.close()
e = int(e_str)
n = int(n_str)
c = int(c_str)
d_max = pow(n , 1/4) / 3
print("d should be less than ", str(d_max))
d = owiener.attack(e, n)
print("d =", d)
m = pow(c, d, n)
flag = long_to_bytes(m)
print(flag)
