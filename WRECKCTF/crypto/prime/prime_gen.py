#!/usr/bin/env python3

from Crypto.Util.number import *
from pwn import *
from sympy import *

context.log_level = "DEBUG"

def main():
	p = remote('challs.wreckctf.com', 31273)
	p.sendlineafter(b'>>', str(getPrime(1024)))
	for i in range(70):
		p.sendlineafter(b'>>',b'1')
	p.interactive()

if __name__ == '__main__':
	main()
