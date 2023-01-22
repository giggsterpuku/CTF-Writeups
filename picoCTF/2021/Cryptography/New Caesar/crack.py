import string

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]

def b16_decode(code):
	decoded = ""
	for c in range(0, len(code), 2): #code[::2]: my init soln wouldn't work
		bin1 = "{0:04b}".format(ALPHABET.index(code[c]))
		bin2 = "{0:04b}".format(ALPHABET.index(code[c + 1])) #code.index(c) + 1])) <- did not take into account mult instances of a char in char code
		binary = bin1 + bin2
		#print(binary)
		#print(bin1, bin2, int(binary, 2))
		decoded += chr(int(binary, 2))
	return decoded

def reverse_shift(c, k):
	t1 = ord(c) - LOWERCASE_OFFSET
	t2 = ord(k) - LOWERCASE_OFFSET
	return ALPHABET[(t1 - t2) % len(ALPHABET)]

ciphertext = "kjlijdliljhdjdhfkfkhhjkkhhkihlhnhghekfhmhjhkhfhekfkkkjkghghjhlhghmhhhfkikfkfhm"
key = "e"
assert all([k in ALPHABET for k in key]) # key comes from truncated alphabet
assert len(key) == 1 # the key is basically a shift like the caesar cipher

#for j in ALPHABET:
#	key = j
dec = ""
for i, c in enumerate(ciphertext):
	dec += reverse_shift(c, key[i % len(key)])
flag = b16_decode(dec)
print(flag)

########################################## Write-Up ##############################################
# Challenge: New Caesar
# Category: Cryptography
# Description: We found a brand new type of encryption, can you break the secret code? (Wrap with picoCTF{}) kjlijdliljhdjdhfkfkhhjkkhhkihlhnhghekfhmhjhkhfhekfkkkjkghghjhlhghmhhhfkikfkfhm new_caesar.py
# Hints:
#	-1: How does the cipher work if the alphabet isn't 26 letters?
#	-2: Even though the letters are split up, the same paradigms still apply
#
# Gist of this new caesar cipher: truncated alphabet, less possible keys (shifts), but idea of caesar cipher is there: the key shifts the alphabet so as to mask the plaintext. In this case, the truncated alphabet is used. The plaintext has more characters than the alphabet, so in the b16() function, it splits each character in the plaintext into two from the truncated alphabet so as to make the shift possible. This script basically reverses the process of encryption, and I used it to find all variations of the flag. The key to the flag is displayed in the key variable.
#
# Flag: picoCTF{et_tu?_1ac5f3d7920a85610afeb2572831daa8}
# Points: 60
# SOlved in picoGym

