#!/usr/bin/env python3

################################ Write-Up ###################################
# Challenge: lambda lambda
# Category: Rev
# Points: 130
# Description: lambda lambda lambda.... lambda? 2692665569775536810618960607010822800159298089096272924
# Hint: Ever hear about lambda calculus?
# Author: preterite
#
# I think there was one real way to solve it, but realistically it would not
# be time-efficient to solve it that way. I first took the advice of the hint
# and learned what lambda calculus is. Basically, it's math notation of
# functions with no name, and you can do stuff with combinations of them,
# such as beta reducing expressions (simplifying them). Looking at the
# chall.py, there were a bunch of lambda functions nested in each other, but
# I was able to figure out that a flag.txt file was read and used to print
# something out. The first strat was to use some beta reductions to simplify
# the functions so that it was easier to read and reverse (this is what I
# think is the real way to solve it), however I realized with so many of
# these functions, it would take a very long time to organize and solve it.
# So, I thought I could maybe blackbox the binary. I made a test flag.txt
# and put some chars in it to be a pretend flag. I ran the script, and it
# pushed out a number. I tried several different "flags" with different
# lengths, including ones containing chars with the "actf{}" flag format,
# and I found that the characters in the actual flag makes a number that is
# similar to the given number that I figured that is the number made by the
# flag when running through chall.py when they are in the correct order (the
# numbers can be seen as similar when compared in hex). I made this script to
# bruteforce the flag char by char so that when it sees the similarities in
# output byte by byte (each char in the flag is represented by a byte in the
# outputted number), it forms the flag eventually. Kinda sad way to solve
# this chall, but it was good in helping me learn lambda calulus.
#
# *Sidenote* if you want to learn lambda calc, see here:
# https://www.simonholywell.com/post/the-lambda-calculus/
#
# Solved by: Ryan Nguyen
# Solved at: after competition
# Flag: actf{3p1c_0n3_l1n3r_95}
#############################################################################
import os

def main():
	flag = "actf{3p1c_0n3" # was just empty but there was a char where the script broke
	endVal = 2692665569775536810618960607010822800159298089096272924
	endHex = str(hex(endVal))
	flagLen = int((len(endHex) - 4) / 2)
	endHexInd = 4 + (len(flag) * 2)
	for i in range(flagLen - len(flag)):
		goal = endHex[:endHexInd]
		#print(goal)
		char = 33
		currentVal = ""
		while goal != currentVal:
			flagFile = open("./flag.txt", "w")
			flagFile.write(flag + chr(char))
			flagFile.close()
			os.system("python3 ./chall.py > out")
			out = open("./out", "r")
			currentVal = str(hex(int(out.read()[:-1])))
			out.close()
			#print(currentVal)
			char += 1
		flag += chr(char - 1)
		#print(flag)
		endHexInd += 2
	print(flag)

if __name__ == "__main__":
	main()
