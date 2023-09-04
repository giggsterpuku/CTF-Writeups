#!/usr/bin/env python3

from sympy.ntheory.modular import crt # Implement Chinese Remainder Theorem

palette = '.=w-o^*'
canvas = list(open('./output.txt', 'r').read())

msg = ''
n = [2, 3, 5, 7] # Moduli

for i in range(225): # 900 non-space and non-newline characters / 4 = 225
	r = [] # Residues
	for m in n:
		while True:
			t = canvas.pop(0)
			if t in palette:
				r.append(palette.index(t))
				break
	x = crt(n,r, check=False)
	msg += chr(x[0])

print(msg)
