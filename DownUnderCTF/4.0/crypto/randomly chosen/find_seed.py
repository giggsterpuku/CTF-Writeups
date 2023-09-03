#!/usr/bin/env python3

import random

filler_flag = "DUCTF{abcdefghijklmnopqrstuvwxyzABEGHIJKLMNOPQRSVWXYZ0123456}" # all characters only used once for no anbiguity in comparisons to find the seed/randomized positions of the flag characters

# Step 1: Find the seed
## Go over a few iterations to filter out the seed actually implemented by comparing the resulting filler string with the actual ciphertext, taking a few characters and comparing their positions to the resulting strings from the random.choice() operations

candidates1 = []

for i in range(1337):
	random.seed(i)
	out = ''.join(random.choices(filler_flag, k=305))
	if out[50] == "{":
		print(f"Potential 1st round seed number: {i}")
		candidates1.append(i)

candidates2 = []

for candidate in candidates1:
	random.seed(candidate)
	out = ''.join(random.choices(filler_flag, k=305))
	if out[32] == "}":
		print(f"Potential 2nd round seed number: {candidate}")
		candidates2.append(candidate)

candidates3 = []

for candidate in candidates2:
	random.seed(candidate)
	out = ''.join(random.choices(filler_flag, k=305))
	if out[1] == "D":
		print(f"Potential 3rd round seed number: {candidate}")
		candidates3.append(candidate)


actual_seed = candidates3[0]
random.seed(actual_seed)
ct = "bDacadn3af1b79cfCma8bse3F7msFdT_}11m8cicf_fdnbssUc{UarF_d3m6T813Usca?tf_FfC3tebbrrffca}Cd18ir1ciDF96n9_7s7F1cb8a07btD7d6s07a3608besfb7tmCa6sasdnnT11ssbsc0id3dsasTs?1m_bef_enU_91_1ta_417r1n8f1e7479ce}9}n8cFtF4__3sef0amUa1cmiec{b8nn9n}dndsef0?1b88c1993014t10aTmrcDn_sesc{a7scdadCm09T_0t7md61bDn8asan1rnam}sU"
#print(ct)

# Step 2: Map the original characters of the flag to their respective positions in the ciphertext, use a demo string to see where the characters land

out = ''.join(random.choices(filler_flag, k=305))

#print(out)

resIdxs = [0 for x in range(305)]

for i, c in enumerate(out):
	resIdxs[i] = filler_flag.index(c)

print(resIdxs)

flag = ''

for i in range(61):
	print(resIdxs.index(i))
	flag += ct[resIdxs.index(i)]

print(flag)
