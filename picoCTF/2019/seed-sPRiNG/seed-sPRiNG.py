#!/usr/bin/env python3

from pwn import *
import ctypes

exe = ELF("seed_spring")
context.binary = exe
libc = ctypes.cdll.LoadLibrary("/lib/x86_64-linux-gnu/libc.so.6")
context.log_level = 'debug'

################################### Write-Up ###################################
# Category: Binary Exploitation
# Points: 350
# Description: The most revolutionary game is finally available: seed sPRiNG is open right now! seed_spring. Connect to it with nc jupiter.challenges.picoctf.org 34558.
#
# This chall was very interesting in its approach other than the normal memory
# corruption stuff for pwn. Tbh it seems more like reversing. So unpacking the
# decompiled code, it seems that we have to correctly guess a randomized
# value 30 consecutive times to get the flag. Seems like a fat chance right?
# Well, the title name gives us a hint at the way we can crack the program.
# As the capital letters suggest (PRNG), the idea is that we are dealing with a
# Predictable Random Number Generator. In the decompiled code, srand() is called
# with a seed (number needed for randomization) from time(0). time(0) puts out
# a number based on the seconds since January 1, 1970, but that info doesn't
# matter. The key is that rand(), which uses srand() to generate numbers from
# the seed, uses a predictable algorithm that spits pseudo-random (not totally
# random) numbers. The win con is that if we can emulate the seed and rand()
# number generation, we will get the same randomized numbers as those from the
# program. We can use the ctypes module to run these C funtions to do it,
# repeat it 30 times, and get our flag.
#
# Flag: picoCTF{pseudo_random_number_generator_not_so_random_81b0dd7e} (from PicoGym)
#
###############################################################################

def conn():
	if False:
		return process([exe.path])
	else:
		return remote("jupiter.challenges.picoctf.org", 34558)
		#return  remote("2019shell1.picoctf.com", 4160)


def main():
	r = conn()
	libc.srand(libc.time(0))
	for i in range(30):
		r.recvuntil("height: ")
		r.sendline(str(libc.rand() & 0xf))
	r.interactive()


if __name__ == "__main__":
	main()
