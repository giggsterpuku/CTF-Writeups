#!/usr/bin/env python3

import string
from Crypto.Util.number import long_to_bytes

alphabet = string.ascii_lowercase + string.ascii_uppercase

f = open('input.txt', 'r')
input = f.read()

print(long_to_bytes(int(input) * 5))
