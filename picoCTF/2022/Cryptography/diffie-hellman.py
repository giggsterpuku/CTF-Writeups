#!/usr/bin/env python3

################################## Write-Up ####################################
# Challenge: diffie-hellman
# Category: Cryptography
# Description: Alice and Bob wanted to exchange information secretly. The two of them agreed to use the Diffie-Hellman key exchange algorithm, using p = 13 and g = 5. They both chose numbers secretly where Alice chose 7 and Bob chose 3. Then, Alice sent Bob some encoded text (with both letters and digits) using the generated key as the shift amount for a Caesar cipher over the alphabet and the decimal digits. Can you figure out the contents of the message? Download the message here. Wrap your decrypted message in the picoCTF flag format like: picoCTF{decrypted_message}
# Hints:
#	-1: Diffie-Hellman key exchange is a well known algorithm for generating keys, try looking up how the secret key is generated
#	-2: For your Caesar shift amount, try forwards and backwards.
#
# Chall was harder than it should have been. The key generation for the Diffie
# Hellman key exchange is implemented in the script, and the key I found was 5.
# The trouble I had was with shifting the phrase around, as I though at first
# you had the shift the numbers and letters separately with different moduli
# (10 and 26 bc of the number of chars per respective group), and I kept getting
# the wrong flag. However, after guessing a bunch, I realized that maybe making
# a custom alphabet might do the trick, and it did. The main thin I learned from
# the chall is that Diffie Hellman creates a secret key using a base g and
# modulus p made public, and those are used with the private keys of two
# individuals using the DH key exchange to create a symmetric, secret key
# without having anyone know the private keys as long as they are not shown in
# public. Some fragments of the key generation are done publicly, but there
# are crucial pieces missing that do not allow anyone else other than the
# individuals to know the private keys, well at the least it makes it very
# difficult.
#
# Flag: picoCTF{C4354R_C1PH3R_15_4_817_0U7D473D_3A2BF44E}
# Points: 200
# Solved by giggsterpuku 2 days into comp
###############################################################################

# Diffie Hellman key generation
p = 13
g = 5
a = 7 # Alice's private key
b = 3 # Bob's private key

A = pow(g, a, p) # the value Alice would send to Bob
# B = pow(g, b, p) <- the value Bob would send to Alice
s =  pow(A, b, p) # how Bob creates the secret
# s = pow(B, a , p) <- how Alice creates the secret
print(s) # calculated to be 5

c = "H98A9W_H6UM8W_6A_9_D6C_5ZCI9C8I_8F7GK99J"
alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
flag = ''

for elem in c:
	if (not elem == "_"):
		flag += alphabet[(alphabet.index(elem) - 5) % 36]
	else:
		flag += elem
print(flag)
