#!/usr/bin/env python
import zlib
IHDR = "\x49\x48\x44\x52\x00\x00\x00\x00\x00\x00\x00\x00\x08\x06\x00\x00\x00"
for w in range(2000):
	for h in range(2000):
		test_string = bytes(IHDR[:4], 'utf-8') + w.to_bytes(4, 'big') +  h.to_bytes(4, 'big') + bytes(IHDR[12:], 'utf-8')
		#print(test_string)
		if (zlib.crc32(test_string) == 0x60444cb6):
			print("Correct size: W:" + str(w) + " x H:" + str(h))
