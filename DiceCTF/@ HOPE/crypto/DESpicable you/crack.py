#!/usr/bin/env python2.7

import string


def encipher(a,b):
	c = ''
	for i, j in zip(a,b):
		c+=chr(ord(i)^ord(j))
	return c

def rekey(key):
	k = ""
	for i,c in enumerate(key):
		if i == len(key)-1:
			k += c
			k += chr(ord(c)^ord(key[0]))
		else:
			k += c
			k += chr(ord(c)^ord(key[i+1]))
	key = k

def des(ct, k):
	i = 0
	p = ''
	while i < len(ct):
		#print(k)
		p += encipher(ct[i:i+len(k)],k)
		i += len(k)
		rekey(k)
	return p

def someascii(s):
	for i, c in enumerate(s):
		if i < len(s) - 1:
			if not (c in string.printable):
				return False
	return True

def main():
	with open('output.txt') as f:
                ciphertext = f.read()

	for i in string.printable:
		for j in string.printable:
			for k in string.printable:
				test_part_pt = "hope{" + i + j + k
				test_key = encipher(ciphertext[:8], test_part_pt)
				result = des(ciphertext, test_key)
				if someascii(result):
					print("Possible flag: %s" % result)
					print("Possible key: %s" % test_key)

main()
