#!/usr/bin/env python3

import os
from pwn import *

flag = "flag{"
lines = []
stillGoing = True
lineNum = 11
while stillGoing:
	stillGoing = False
	for i in range(33,127):
		output = flag + chr(i)
		cmd = 'echo ' + output + ' > not_even_real.txt'
		os.system(cmd)
		os.system('ltrace --output output.txt ./app')
		with open("output.txt") as f:
			lines = f.readlines()
		print(lines[lineNum])
		if '= 10' in lines[lineNum]:
			flag += chr(i)
			print('Flag: ' + flag)
			lineNum += 2
			stillGoing = True
			break

# This was the script I used to try to bruteforce the flag. Bruh.
