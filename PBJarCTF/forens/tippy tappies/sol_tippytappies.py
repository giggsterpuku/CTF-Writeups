#!/usr/bin/env python3

#################################### Write-Up ##################################
#
# Challenge: tippy tappies
# Category: forens
# Description: how'd you get this in the first place :eyes: dids you has logger on me?
# Author: ZeroDayTea
#
# I saw the packets on Wireshark and saw that the packets are using a USB
# protocol, but I was not sure what to do with it. Funny enough, my YouTube recs
# gave this blessed video of Lord John Hammond doing a similar chall in picoCTF
# 2017: https://www.youtube.com/watch?v=0HXL4RGmExo&ab_channel=JohnHammond. The
# key here is that there is "leftover data" in packets starting from packet 65,
# and a byte inside the data corresponds to the to a USB HID table, which has
# values that correspond to keys on a keyboard/any other Human Input Device
# (hence HID). So, I grabbed a table from online and used it in this script in
# a dictionary. From there, I learned to use the python module scapy from the
# video and translate the keyboard codes into readable text. From there, I was
# able to obtain and figure out the flag.
#
# Solved by: Ryan Nguyen
# Solved at: after competition
# Points: 288
# Flag: flag{wowgoodusbdetectivework}
################################################################################

from scapy.all import *

t = rdpcap("./tippytappies.pcapng")
mapping = {0x0 : "", 0x04 : "a", 0x05 : "b", 0x06 : "c", 0x07 : "d", 0x08 : "e", 0x09 : "f", 0x0A : "g", 0x0B : "h", 0x0C : "i", 0x0D : "j", 0x0E : "k", 0x0F : "l", 0x10 : "m", 0x11 : "n", 0x12 : "o", 0x13 : "p", 0x14 : "q", 0x15 : "r", 0x16 : "s", 0x17 : "t", 0x18 : "u", 0x19 : "v", 0x1A : "w", 0x1B : "x", 0x1C : "y", 0x1D : "z", 0x1E : "1", 0x1F : "2", 0x20 : "3", 0x21 : "4", 0x22 : "5", 0x23 : "6", 0x24 : "7", 0x25 : "8", 0x26 : "9", 0x27 : "0", 0x28 : "", 0x29 : "", 0x2A : "", 0x2B : "", 0x2C : " ", 0x2D : "-", 0x2E : "=", 0x2F : "[", 0x30 : "]", 0x31 : "\\", 0x32 : "#", 0x33 : ";", 0x34 : "‘", 0x35 : "~", 0x36 : ",", 0x37 : ".", 0x38 : "/"}
typed = " "

packet = 64
for i in range(1254):
	hid = t[packet].load[-6]
	char = mapping[hid]
	if char != typed[-1]:
		typed += char
	hid = t[packet].load[-5]
	char = mapping[hid]
	if char != typed[-1]:
		typed += char
	#print(typed)
	packet += 1
print(typed)
