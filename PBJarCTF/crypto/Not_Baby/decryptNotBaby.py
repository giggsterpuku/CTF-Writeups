#!/usr/bin/env python3

################################## Write-Up ####################################
# Challenge: Not_Baby
# Category: crypto
# Description: Hmm.... What is this?
# Author: QuickMaffs
#
# Looking at the script, I knew that the way to decrypt the message was a varied
# version of RSA, but the thing you need to do this time is to find the factors
# in the n given in out.txt. So, the idea is that the phi (orginally lambda n
# in the last chall) is a product of all the prime factors of n - 1, so it's
# no longer the traditional p and q being take into account. By doing that, the
# rest of the chall was like the rest of the RSA steps: get d and then use it
# to get the plaintext by doing ct^d mod n.
#
# Flag: flag{f4ct0ring_s0000oo00000o00_h4rd}
# Points: 283
# Solved by: Ryan Nguyen
# Solved at: after comp
################################################################################

from Crypto.Util.number import *


#From out.txt
n = 57436275279999211772332390260389123467061581271245121044959385707165571981686310741298519009630482399016808156120999964
e =  65537
ct =  25287942932936198887822866306739577372124406139134641253461396979278534624726135258660588590323101498005293149770225633
# factors taken from online factorization database factordb.com (remember that factors must be prime for RSA to work)
factors = [2, 2, 73, 181, 11411, 235111, 6546828737292350227122068012441477, 61872434969046837223597248696590986360784288448775988338706090668799371]
phi = 1
for i in factors: # Each factor must be take into account to solve for phi
	phi *= (i - 1)
#print(phi) -> 14082829955730492424779991816751826783740419821222049896685159828122233141863798636992766727674089919451714351771520000
d = 7127690764477782530935995369968996054391713466742990907015071661791270172812643251736424803652128761283143339613673473 # Extended Euclidean Algorithm (find d such that e * d mod phi = 1)
m = pow(ct, d, n)
flag = long_to_bytes(m)

print(flag)
