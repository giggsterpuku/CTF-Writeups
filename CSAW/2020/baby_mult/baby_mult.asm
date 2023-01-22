; This is x86_64 Intel, kinda got the wrong one earlier (just x86) and noticed since some vars went undefined hm
0:  55                      push   rbp
1:  48 89 e5                mov    rbp,rsp
4:  48 83 ec 18             sub    rsp,0x18
8:  48 c7 45 f8 4f 00 00    mov    QWORD PTR [rbp-0x8],0x4f
f:  00
10: 48 b8 15 4f e7 4b 01    movabs rax,0x14be74f15
17: 00 00 00
1a: 48 89 45 f0             mov    QWORD PTR [rbp-0x10],rax
1e: 48 c7 45 e8 04 00 00    mov    QWORD PTR [rbp-0x18],0x4
25: 00
26: 48 c7 45 e0 03 00 00    mov    QWORD PTR [rbp-0x20],0x3
2d: 00
2e: 48 c7 45 d8 13 00 00    mov    QWORD PTR [rbp-0x28],0x13
35: 00
36: 48 c7 45 d0 15 01 00    mov    QWORD PTR [rbp-0x30],0x115
3d: 00
3e: 48 b8 61 5b 64 4b cf    movabs rax,0x77cf4b645b61
45: 77 00 00
48: 48 89 45 c8             mov    QWORD PTR [rbp-0x38],rax
4c: 48 c7 45 c0 02 00 00    mov    QWORD PTR [rbp-0x40],0x2
53: 00
54: 48 c7 45 b8 11 00 00    mov    QWORD PTR [rbp-0x48],0x11
5b: 00
5c: 48 c7 45 b0 c1 21 00    mov    QWORD PTR [rbp-0x50],0x21c1
63: 00
64: 48 c7 45 a8 e9 65 22    mov    QWORD PTR [rbp-0x58],0x182265e9
6b: 18
6c: 48 c7 45 a0 33 08 00    mov    QWORD PTR [rbp-0x60],0x833
73: 00
74: 48 c7 45 98 ab 0a 00    mov    QWORD PTR [rbp-0x68],0xaab
7b: 00
7c: 48 c7 45 90 ad aa 8d    mov    QWORD PTR [rbp-0x70],0x8daaad
83: 00
84: 48 8b 45 f8             mov    rax,QWORD PTR [rbp-0x8]
88: 48 0f af 45 f0          imul   rax,QWORD PTR [rbp-0x10]
8d: 48 89 45 88             mov    QWORD PTR [rbp-0x78],rax
91: 48 8b 45 e8             mov    rax,QWORD PTR [rbp-0x18]
95: 48 0f af 45 e0          imul   rax,QWORD PTR [rbp-0x20]
9a: 48 0f af 45 d8          imul   rax,QWORD PTR [rbp-0x28]
9f: 48 0f af 45 d0          imul   rax,QWORD PTR [rbp-0x30]
a4: 48 0f af 45 c8          imul   rax,QWORD PTR [rbp-0x38]
a9: 48 89 45 80             mov    QWORD PTR [rbp-0x80],rax
ad: 48 8b 45 c0             mov    rax,QWORD PTR [rbp-0x40]
b1: 48 0f af 45 b8          imul   rax,QWORD PTR [rbp-0x48]
b6: 48 0f af 45 b0          imul   rax,QWORD PTR [rbp-0x50]
bb: 48 0f af 45 a8          imul   rax,QWORD PTR [rbp-0x58]
c0: 48 89 85 78 ff ff ff    mov    QWORD PTR [rbp-0x88],rax
c7: 48 8b 45 a0             mov    rax,QWORD PTR [rbp-0x60]
cb: 48 0f af 45 98          imul   rax,QWORD PTR [rbp-0x68]
d0: 48 0f af 45 90          imul   rax,QWORD PTR [rbp-0x70]
d5: 48 89 85 70 ff ff ff    mov    QWORD PTR [rbp-0x90],rax
dc: b8 00 00 00 00          mov    eax,0x0
e1: c9                      leave
