#!/usr/bin/env python3

###################################################################### Write-Up #####################################################################
# Challenge: Hex
# Category: Cryptography
# Description: Cryptograms == encryption, right? Flag is readable English.
#
# From looking at the source code of the encryption scheme, the chall was to decrypt the substitution cipher of a hex encoding of the flag. Not too
# bad, but interesting to do a bit of guessing around to get the flag.
#
# Flag: ictf{military_grade_encoding_ftw}
# Points: 100
# Solved by giggsterpuku 2 days 8 hrs into comp
#####################################################################################################################################################

from Crypto.Util.number import *

#     696374667b6d696c69746172795f67726164655f656e636f64696e675f6674777d
ct = '0d0b18001e060d090d1802131dcf011302080ccf0c070b0f080d0701cf00181116'
key = { '0' : '6', '1' : '7', '2' : '1', '3' : '2', '4' : '', '5' : '', '6' : 'd', '7' : 'e', '8' : '4', '9' : 'c', 'a' : '', 'b' : '3', 'c' : '5', 'd' : '9', 'e' : 'b', 'f' : 'f'} # no val for some bc some digits unused in ciphertext
flag = ''

for c in ct:
	''' for testing key
	if (key[c] == ''):
		flag += c
	else:
		flag += key[c]
	'''
	flag += key[c]

print(long_to_bytes(int(flag, 16)))
