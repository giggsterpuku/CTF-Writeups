#!/usr/bin/env python3

################################# Write-Up #####################################
# Challenge: RAIId Shadow Legends
# Category: Binary
# Points: 100
# Description: I love how C++ initializes everything for you. It makes things so easy and fun! Speaking of fun, play our fun new game RAIId Shadow Legends (source) at /problems/2021/raiid_shadow_legends on the shell server, or connect with nc shell.actf.co 21300.
# Hint: Resource acquisition is initialization, so everything I acquired should be initialized, right?
# Author: kmh
#
# So I kinda solved this just by playing around and not understanding what RAII
# is, but I found out after solving what it was and how it applied to the chall.
# Running through the program, it seems like a game. You are prompted to start
# the game or buy shadow tokens used to increase your skill level, but you can't
# do that since you "have to pay" somewhere else. When you start, you are
# prompted to sign and agree to terms and conditions. Then, you have 3 choices:
# power up, fight, or quit the game. You can't power up to increase your skill
# level, and you will always lose if you fight, so there's not much you can do
# (with intended input). Looking at the source code, you can see that in order
# to snag the flag, you need your skill level to be 1337, but you can't change
# it at all and it will stay 0 (again, with intended input). So, I monkeyed
# around, putting random input in lots of areas, and then I discovered that
# if you input more than 4 chars into the agreement variable (where you say
# "yes" to terms and conditions), after signing and making a username the skill
# level then changes. I got the number of the skill level and turned it to hex
# and found that the chars after the 4th char were interpreted as decimal and
# formatted in Little Endian, so what I needed to do was input 4 chars followed
# by 1337 in hex and Little Endian to change the skill level. Then, just
# filling out the rest and "fighting," I solved the chall. I later looked more
# into RAII (as referred to by the chall name and hint), and I learned it was a
# C++ technique where the program saved resources (ie memory) after the
# initialization of data structures and before their finalization (destruction).
# In other words, as long as an intialized data structure exists, its resources
# are reserved for it and can be used in the program, no matter if its in or
# out of a scope of a function. However, the catch is that the data structure
# MUST be initialized. In the source code, you can see the agreement variable
# was not declared (with a = , it had the << thing), so it was not initialized.
# Therefore, when the character structure is initialized (since it was
# declared), the data that was made for the agreement var was actually
# tranferred over to the character object. Thus, the input overwrote its vars.
# So, since the int vars (health and skill) are by default 4 bytes long, the
# "yes"/filler bytes we put in for the agreement part actually turned into the
# value of health, and the part we put in for the 1337 skill level landed in the
# skill variable. Neat chall, interesting concept.
#
# Solved by: Ryan Nguyen
# Solved at: after competition
# Flag: server down, so no flag T_T
################################################################################

from pwn import *

exe = ELF("raiid_shadow_legends")

context.binary = exe

def main():
	r = process([exe.path])
	r.recvuntil('What would you like to do?')
	r.sendline('1')
	r.recvuntil('Do you agree to the terms and conditions?')
	r.sendline('2222' + '\x39\x05')
	r.recvuntil('Do you agree to the terms and conditions?')
	r.sendline('yes')
	r.recvuntil('Sign here:')
	r.sendline('shrimp')
	r.recvuntil('Enter your name:')
	r.sendline('Gawr Gura')
	r.recvuntil('What would you like to do?')
	r.sendline('2')
	r.interactive()

if __name__ == "__main__":
	main()
