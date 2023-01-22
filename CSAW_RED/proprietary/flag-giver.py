#!/usr/bin/env python3

string1 = "pleasegivemunneytousedis"
string2 = "nofreelunches-orsoftware"
string3 = "supersupersupersecretdrm"
flag = ""

for i in range(24):
	s = ord(string1[i]) ^ ord(string2[i])
	s = s ^ ord(string3[i])
	flag += chr(s)
print(flag)
