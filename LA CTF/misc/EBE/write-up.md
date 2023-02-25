# Challenge: EBE

**Category:** misc

**Description:** I was trying to send a flag to my friend over UDP, one character at a time, but it got corrupted! I think someone else was messing around with me and sent extra bytes, though it seems like they actually abided by RFC 3514 for once. Can you get the flag?

The idea of the challenge is to filter out packets that have a security flag set as not evil for IPv4 and extract the data at the end of each packet. The description suggets the RFC 3514 standard, which has do with setting an "evil" bit/security flag in the flags field of the packet. If it is set to 1, the packet is "evil,"
meaning its contents have malicious intent, and if set to 0, it is interpreted to be harmless data. To apply RFC 3514 in Wireshark, I set the preferences for the IPv4 protocol to interpret the reserved flag as the security flag. In addition, the filter I applied to filter out the not "evil" packets was ip.flags.sf == 0, and then I extracted the data field out of each packet to get the flag.



Flag: lactf{3V1L_817_3xf1l7R4710N_4_7H3_W1N_51D43c8000034d0c}
Solved by giggsterpuku
