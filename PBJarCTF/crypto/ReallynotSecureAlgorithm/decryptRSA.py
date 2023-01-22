#!/usr/bin/env python3

################################## Write-Up ####################################
# Challenge: ReallyNotSecureAlgorithm
# Category: crypto
# Description: Here's the obligatory problem!!!
# Author: QuickMaffs
#
# I know this was a traditional RSA decryption chall, but I wanted to learn a
# bit more about how the encryption scheme worked, so I looked up some stuff on
# Wikipedia. The script.py is an accurate prepresentation of how it works, so I
# tried to reverse it as best as I could here so that I could apply what the
# Wikipedia article explained in this script. I will look more into this after
# this CTF.
#
# Flag: flag{n0t_to0_h4rd_rIt3_19290453}
# Points: 289 (at time of solve)
# Solved by: Ryan Nguyen
# Solved at: 4 hours into competition
################################################################################

from Crypto.Util.number import *

#From out.txt
e = 65537
p = 194522226411154500868209046072773892801
q = 288543888189520095825105581859098503663
ct = 2680665419605434578386620658057993903866911471752759293737529277281335077856
n = p * q
lambda_n = (p - 1) * (q - 1)
d = 39365191632547732007914614856903809984286421688048990897845086680417895132673# solve using modular inverse equation (d * e) % lambda_n = 1
m = pow(ct, d, n)
flag = long_to_bytes(m)

print(flag)
