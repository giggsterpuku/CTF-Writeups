#!/usr/bin/env python3

################################ Write-Up #################################
# Challenge: Very Smooth
# Category: Cryptography
# Description: Forget safe primes... Here, we like to live life dangerously... >:) gen.py output.txt
# Hints:
#	-1: Don't look at me... Go ask Mr. Pollard if you need a hint!
#
# Looking at the n value of what seems to be an RSA chall, I saw it was a
# HUGE number and that me trusty tools factordb and yafu could not pull
# a factorization feat. However, looking at the hint and the chall name,
# I Googled "Pollard RSA" and found the algorithm that would help me
# break this chall: Pollard's p - 1 algorithm. This is a special algorithm
# that quickly factorized numbers so long as a number one less than a
# factor (hence p - 1) is a powersmooth prime (factor that is less than
# or equal to a number, ie 5 is 17-smooth since it is prime and less than
# 17). I found an implementation of the algorithm on Geeksforgeeks, and
# it gave me the first prime in less than 30 sec. I was stuck on this for
# so long not realizing that my code worked; I didn't test it at all until
# now :see_no_evil:. Welp, it does. As a side note, looking at the gen.py
# code, you can see that the "smoothness" of a number is applied to the
# finding of the prime numbers, so that's another indicator of using
# the p - 1 alg. Do that to get the primes, and the rest is RSA descrypt.
#
# Flag: picoCTF{7c8625a1}
# Points: 300
# Solved by giggsterpuku 5 days into comp
###########################################################################

import math
import sympy
from Crypto.Util.number import *
# Note for next time: try decimal module for more precise calculations (at least for division)

n = 0xc5261293c8f9c420bc5291ac0c14e103944b6621bb2595089f1641d85c4dae589f101e0962fe2b25fcf4186fb259cbd88154b75f327d990a76351a03ac0185af4e1a127b708348db59cd4625b40d4e161d17b8ead6944148e9582985bbc6a7eaf9916cb138706ce293232378ebd8f95c3f4db6c8a77a597974848d695d774efae5bd3b32c64c72bcf19d3b181c2046e194212696ec41f0671314f506c27a2ecfd48313e371b0ae731026d6951f6e39dc6592ebd1e60b845253f8cd6b0497f0139e8a16d9e5c446e4a33811f3e8a918c6cd917ca83408b323ce299d1ea9f7e7e1408e724679725688c92ca96b84b0c94ce717a54c470d035764bc0b92f404f1f5
c = 0x1f511af6dd19a480eb16415a54c122d7485de4d933e0aeee6e9b5598a8e338c2b29583aee80c241116bc949980e1310649216c4afa97c212fb3eba87d2b3a428c4cc145136eff7b902c508cb871dcd326332d75b6176a5a551840ba3c76cf4ad6e3fdbba0d031159ef60b59a1c6f4d87d90623e5fe140b9f56a2ebc4c87ee7b708f188742732ff2c09b175f4703960f2c29abccf428b3326d0bd3d737343e699a788398e1a623a8bd13828ef5483c82e19f31dca2a7effe5b1f8dc8a81a5ce873a082016b1f510f712ae2fa58ecdd49ab3a489c8a86e2bb088a85262d791af313b0383a56f14ddbb85cb89fb31f863923377771d3e73788560c9ced7b188ba97

def pollard(num):
	a = 2
	i = 1
	while True:
		a = pow(a, i, num)
		d = math.gcd((a - 1), num)
		if (d > 1):
			return d
			break
		i += 1

def find_primes(num): # accurate in concept, bad w/ finding 2nd prime
	t = num # temp storage for n to be used to find primes
	ans = []
	while True:
		d = pollard(t)
		ans.append(d)
		print(ans)
		#print(math.floor(t / d))
		#print(math.ceil(t / d))
		r = int(t / d) # this thing gave me an inaccurate 2nd factor so i used a beeg calculator
		if (sympy.isprime(r)):
			ans.append(r)
			return ans
		else:
			t = r

e = 0x10001
p = pollard(n)
q = 155886972960664534013041814351782927840465950022742711153704061512767231252254923859358385447688708709761645561788434482490726299524712681978677060822069411804436435368518028882769406676617745559724738774782701625211779174370759988895228070938831967483401953816901269670197361506466713077188578114638897325343 #from the big calculator
phi = (p - 1) * (q - 1)
d = sympy.mod_inverse(e, phi)
m = pow(c, d, n)

print(long_to_bytes(m))
