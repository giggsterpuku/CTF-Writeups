#!/usr/bin/env python3

################################## Write-Up ####################################
# Challenge: Infinity Gauntlet
# Category: Rev
# Points: 75
# Description: All clam needs to do is snap and finite will turn into infinite... Find it on the shell server at /problems/2021/infinity_gauntlet or over netcat at nc shell.actf.co 21700.
# Author: aplet123
#
# Running it for the first time, I found that the program is one that had you
# solve for an unknown nubmer in some foo()/bar() functions. Opening it in
# Ghidra, I initially saw that the foo/bar fxns were mathematical equations, so
# basically the job was to do the algebra to get the answers. I learned and used
# SymPy to solve some of them. I also saw a condition that if you passed Round
# 50 it would do something, and to me I thought it would give the flag. Later
# I realized I read the code too shallowly, as there was no flag presented to
# my screen. :( So, I looked at the code again, and I saw that Rounds 50+ would
# reveal some parts of the flag in random order and encrypt the characters.
# Looking at it for a few more hours and looking at writeups, I figured that
# the number, in hex, would reveal two things: the position of the char in the
# flag in the"upper" byte and the encrypted char in the "lower" one. The code
# also reveals how the char is encrypted: XORing 17 * the position of the char
# in the flag. Putting it all together, I made the script make two lists: one
# for the indexes and one for the unencrypted chars. Then, after many iterations
# of crunching numbers, you can take the lists and figure out the flag by hand.
#
# Solved by: Ryan Nguyen (past competition for review)
# Flag: <Chall servers shut down ;-;>
################################################################################

from pwn import *
from sympy.solvers import solve
from sympy import Symbol
from sympy.logic.boolalg import Xor
exe = ELF("infinity_gauntlet")

context.binary = exe

def main():
	r = process([exe.path])
	n = Symbol('n')
	r.recvline()
	flag = []
	ind = []
	for i in range(300):
		ans = 0
		r.recvline()
		r.recvline()
		eq = r.recvline().decode('utf-8')
		print(eq)
		front_paren = 3
		back_paren = eq.index(')')
		equal = eq.index('=')
		first_comma = eq.index(',')
		if "foo" in eq:
			# solve foo expression
			x = eq[front_paren + 1 : first_comma]
			y = eq[first_comma + 2 : back_paren]
			a = eq[equal + 2 :]
			if x == "?":
				x = n
				y = int(y)
				a = int(a)
				ans = (str(a ^ (y + 1) ^ 1337))
				r.sendline(ans)
			elif y == "?":
				y = n
				x = int(x)
				a = int(a)
				ans = (str((a ^ x ^ 1337) - 1))
				r.sendline(ans)
			else:
				a = n
				y = int(y)
				x = int(x)
				ans = (str((y + 1) ^ x ^ 1337))
				r.sendline(ans)
			#print(x, y, a)
		if "bar" in eq:
			# solve bar expression
			second_comma = eq.index(',', first_comma + 1)
			x = eq[front_paren + 1 : first_comma]
			y = eq[first_comma + 2 : second_comma]
			z = eq[second_comma + 2 : back_paren]
			a = eq[equal + 2 :]
			if x == "?":
				x = n
				y = int(y)
				z = int(z)
				a = int(a)
			elif y == "?":
				y = n
				x = int(x)
				z = int(z)
				a = int(a)
			elif z == "?":
				z = n
				x = int(x)
				y = int(y)
				a = int(a)
			else:
				a = n
				y = int(y)
				z = int(z)
				x = int(x)
			#print(x, y, z, a)
			ans = (str(solve((z + 1) * y + x - a, n)[0]))
			r.sendline(ans)
		if (i + 1) > 49:
			hex_ans = str(hex(int(ans)))
			top_byte = int(hex_ans[2:4], 16) # Index of flag char
			bot_byte = int(hex_ans[4:], 16) # Le encrypted char
			pos = top_byte - (i + 1)
			char = chr(bot_byte ^ ((pos * 17) % 256))
			print(char, pos)
			if not pos in ind and pos >= 0:
				ind.append(pos)
				flag.append(char)
			print(ind, flag)
	r.interactive()

if __name__ == "__main__":
	main()
