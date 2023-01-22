#!/usr/bin/env python3

posibilities1 = ['T', 'C', 'A', 'G']
posibilities2 = ['T', 'A', 'C', 'G']
encflag = 'GACGCCTGACCCTTATATGGCGTATCCTTGAGCGGCCCCTAAGATCCCTCAGGGGTTTACGCGGAGACCTCTCAAAGGGTGGTGGCCCCTCAGCGAAGATCGAGTGGCAGCTGTCATGACGATTCATAGGATCCAGACTAGGCCATGA'
rkey = 0x8f
flag = ""

for i in range(len(encflag) // 4):
	seq = encflag[4*i:4*i+4]
	rev_rkey = format(rkey,"08b")[::-1]
	rev_char = ""
	for idx,c in enumerate(seq):
		if (idx < 2):
			twoBit_seq = posibilities1.index(c)
		else:
			twoBit_seq = posibilities2.index(c)
		twoBit_rkey = int(rev_rkey[2*idx:2*idx+2], 2)
		rev_char += format(twoBit_seq ^ twoBit_rkey, "02b")
	flag_char = chr(int(rev_char[::-1], 2))
	flag += flag_char
	rkey = rkey + ord(flag_char) & 0xff
print(flag)
