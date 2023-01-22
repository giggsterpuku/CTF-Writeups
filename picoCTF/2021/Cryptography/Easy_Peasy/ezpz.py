#!/usr/bin/env python3

from pwn import *

flag = bytes.fromhex("5b1e564b6e415c0e394e0401384b08553a4e5c597b6d4a5c5a684d50013d6e4b")
test_string = "\x00" * 32

r = remote("mercury.picoctf.net", 20266)
r.recvuntil("encrypt?")
r.sendline("a" * (50000 - 32))
r.recvuntil("encrypt?")
r.sendline(test_string)
r.recvline()
test_output = r.recvline()[:-1]
r.close()

key = bytes.fromhex(test_output.decode('utf-8'))
ans = ''
for i in range(len(flag)):
	ans += (chr(flag[i] ^ key[i]))
print(ans)

############################################ Write-Up #############################################
# Challenge: Easy Peasy
# Category: Cryptography
# Points: 40
# Description: A one-time pad is unbreakable, but can you manage to recover the flag? (Wrap with picoCTF{}) nc mercury.picoctf.net 20266 otp.py
# Hints:
#	- 1: Maybe there's a way to make this a 2x pad.
#
# I didn't know what a one-time pad (OTP) was, so I looked it up first. In short, it is a encryption that relies on a key of randomness to obfuscate the message being sent, the main concept being that the key must be completely random for the cipher to be effective. Looking at articles and looking at the hint, I initially thought that what I needed to do was get another ciphertext out of the remotel run script and XOR that with the ciphertext to get a string that I could XOR with the test string I inputted so as to unravel the flag. I thought that doing so would remove the key out of the string of information due to XOR properties.
# But I didn't consider that key is 50000 chars long, flag is 32 chars long... (that's what write-ups said) and I COMPLETELY forgot about that :see_no_evil:.
# Key strat: code suggests key_location index incrememted by startup() and encrypt(), just make key_location = 0 w/ your input and get the key segment we need with null bytes
# Remember: null byte xor'ed with a char is the char!

# Flag: picoCTF{99072996e6f7d397f6ea0128b4517c23}
# Solved in picoGym
