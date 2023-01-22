#!/usr/bin/env python3

from pwn import *
import string
from tqdm import tqdm

charset = string.ascii_letters + string.digits + "_{}" # every char to bruteforce
flag = "picoCTF{" # The shortened length of the compression is not noticeable on the first few characters, so this is a better starting point for the bruteforcing.

p = remote("mercury.picoctf.net", 50899)
while not (flag[len(flag) - 1] == "}"):
	min_len = 10000
	min_char = ""
	for c in tqdm(charset):
		try:
			p.sendlineafter("Enter your text to be encrypted: ", flag + c)
			p.recvline()
			p.recvline()
			enc_len = int(p.recvline().strip().decode())
			if (enc_len < min_len):
				min_len = enc_len
				min_char = c
		except:
			p = remote("mercury.picoctf.net", 50899)
	flag += min_char
	print(flag)
print(flag)
p.close()
