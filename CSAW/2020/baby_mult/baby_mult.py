#!/usr/bin/env python3

# This was made to turn the decimal representation of the opcodes into hex for the online disassembler to read
opcode = [85, 72, 137, 229, 72, 131, 236, 24, 72, 199, 69, 248, 79, 0, 0, 0, 72, 184, 21, 79, 231, 75, 1, 0, 0, 0, 72, 137, 69, 240, 72, 199, 69, 232, 4, 0, 0, 0, 72, 199, 69, 224, 3, 0, 0, 0, 72, 199, 69, 216, 19, 0, 0, 0, 72, 199, 69, 208, 21, 1, 0, 0, 72, 184, 97, 91, 100, 75, 207, 119, 0, 0, 72, 137, 69, 200, 72, 199, 69, 192, 2, 0, 0, 0, 72, 199, 69, 184, 17, 0, 0, 0, 72, 199, 69, 176, 193, 33, 0, 0, 72, 199, 69, 168, 233, 101, 34, 24, 72, 199, 69, 160, 51, 8, 0, 0, 72, 199, 69, 152, 171, 10, 0, 0, 72, 199, 69, 144, 173, 170, 141, 0, 72, 139, 69, 248, 72, 15, 175, 69, 240, 72, 137, 69, 136, 72, 139, 69, 232, 72, 15, 175, 69, 224, 72, 15, 175, 69, 216, 72, 15, 175, 69, 208, 72, 15, 175, 69, 200, 72, 137, 69, 128, 72, 139, 69, 192, 72, 15, 175, 69, 184, 72, 15, 175, 69, 176, 72, 15, 175, 69, 168, 72, 137, 133, 120, 255, 255, 255, 72, 139, 69, 160, 72, 15, 175, 69, 152, 72, 15, 175, 69, 144, 72, 137, 133, 112, 255, 255, 255, 184, 0, 0, 0, 0, 201]
bytes = []
shellcode = ''
for i in opcode:
	bytes.append(hex(i))
for i in range(len(bytes)):
	shellcode += "\\x"
	if opcode[i] < 0x10:
		shellcode += "0"
	shellcode += str(bytes[i])[2::]

print(shellcode)

''' Used and online disassembler to make this (wrong asm code)
0:  55                      push   ebp
1:  48                      dec    eax
2:  89 e5                   mov    ebp,esp
4:  48                      dec    eax
5:  83 ec 18                sub    esp,0x18
8:  48                      dec    eax
9:  c7 45 f8 4f 00 00 00    mov    DWORD PTR [ebp-0x8],0x4f
10: 48                      dec    eax
11: b8 15 4f e7 4b          mov    eax,0x4be74f15
16: 01 00                   add    DWORD PTR [eax],eax
18: 00 00                   add    BYTE PTR [eax],al
1a: 48                      dec    eax
1b: 89 45 f0                mov    DWORD PTR [ebp-0x10],eax
1e: 48                      dec    eax
1f: c7 45 e8 04 00 00 00    mov    DWORD PTR [ebp-0x18],0x4
26: 48                      dec    eax
27: c7 45 e0 03 00 00 00    mov    DWORD PTR [ebp-0x20],0x3
2e: 48                      dec    eax
2f: c7 45 d8 13 00 00 00    mov    DWORD PTR [ebp-0x28],0x13
36: 48                      dec    eax
37: c7 45 d0 15 01 00 00    mov    DWORD PTR [ebp-0x30],0x115
3e: 48                      dec    eax
3f: b8 61 5b 64 4b          mov    eax,0x4b645b61
44: cf                      iret
45: 77 00                   ja     0x47
47: 00 48 89                add    BYTE PTR [eax-0x77],cl
4a: 45                      inc    ebp
4b: c8 48 c7 45             enter  0xc748,0x45
4f: c0 02 00                rol    BYTE PTR [edx],0x0
52: 00 00                   add    BYTE PTR [eax],al
54: 48                      dec    eax
55: c7 45 b8 11 00 00 00    mov    DWORD PTR [ebp-0x48],0x11
5c: 48                      dec    eax
5d: c7 45 b0 c1 21 00 00    mov    DWORD PTR [ebp-0x50],0x21c1
64: 48                      dec    eax
65: c7 45 a8 e9 65 22 18    mov    DWORD PTR [ebp-0x58],0x182265e9
6c: 48                      dec    eax
6d: c7 45 a0 33 08 00 00    mov    DWORD PTR [ebp-0x60],0x833
74: 48                      dec    eax
75: c7 45 98 ab 0a 00 00    mov    DWORD PTR [ebp-0x68],0xaab
7c: 48                      dec    eax
7d: c7 45 90 ad aa 8d 00    mov    DWORD PTR [ebp-0x70],0x8daaad
84: 48                      dec    eax
85: 8b 45 f8                mov    eax,DWORD PTR [ebp-0x8]
88: 48                      dec    eax
89: 0f af 45 f0             imul   eax,DWORD PTR [ebp-0x10]
8d: 48                      dec    eax
8e: 89 45 88                mov    DWORD PTR [ebp-0x78],eax
91: 48                      dec    eax
92: 8b 45 e8                mov    eax,DWORD PTR [ebp-0x18]
95: 48                      dec    eax
96: 0f af 45 e0             imul   eax,DWORD PTR [ebp-0x20]
9a: 48                      dec    eax
9b: 0f af 45 d8             imul   eax,DWORD PTR [ebp-0x28]
9f: 48                      dec    eax
a0: 0f af 45 d0             imul   eax,DWORD PTR [ebp-0x30]
a4: 48                      dec    eax
a5: 0f af 45 c8             imul   eax,DWORD PTR [ebp-0x38]
a9: 48                      dec    eax
aa: 89 45 80                mov    DWORD PTR [ebp-0x80],eax
ad: 48                      dec    eax
ae: 8b 45 c0                mov    eax,DWORD PTR [ebp-0x40]
b1: 48                      dec    eax
b2: 0f af 45 b8             imul   eax,DWORD PTR [ebp-0x48]
b6: 48                      dec    eax
b7: 0f af 45 b0             imul   eax,DWORD PTR [ebp-0x50]
bb: 48                      dec    eax
bc: 0f af 45 a8             imul   eax,DWORD PTR [ebp-0x58]
c0: 48                      dec    eax
c1: 89 85 78 ff ff ff       mov    DWORD PTR [ebp-0x88],eax
c7: 48                      dec    eax
c8: 8b 45 a0                mov    eax,DWORD PTR [ebp-0x60]
cb: 48                      dec    eax
cc: 0f af 45 98             imul   eax,DWORD PTR [ebp-0x68]
d0: 48                      dec    eax
d1: 0f af 45 90             imul   eax,DWORD PTR [ebp-0x70]
d5: 48                      dec    eax
d6: 89 85 70 ff ff ff       mov    DWORD PTR [ebp-0x90],eax
dc: b8 00 00 00 00          mov    eax,0x0
e1: c9                      leave
'''
