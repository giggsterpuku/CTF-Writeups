###Challenge: one byte

####Category: pwn

####Description: Here's a one byte buffer overflow!

####Author: joseph

This was a challenge that I can say I learned a lot from, credits to the challenge author for a slightly difficult yet good challenge.

From the looks of the challenge name and description, I figure that I am only able to overflow the buffer by one byte. I don't know about other architectures, but in x86_64 and x86, one byte overwrite outside the buffer only overwrites a byte into the base pointer (a.k.a. the EBP) or a local variable placed on the stack in a higher address, and in my experience you'd usually want to overwrite beyond the EBP and into the instruction pointer (a.k.a. the IP), so I wasn't sure how to take advantage of the one-byte overflow. Looking at the source code, there seems to be an obvious goal: call the win() function, which spawns a shell. Here is the source code for reference:

```c
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

void init() {
    setvbuf(stdout, 0, 2, 0);
    setvbuf(stdin, 0, 2, 0);
}

void win() {
    system("/bin/sh");
}

int main() {
    init();

    printf("Free junk: 0x%lx\n", init);
    printf("Your turn: ");

    char buf[0x10];
    read(0, buf, 0x11);
}
```

As you may notice, the buffer (buf) is 16 bytes in length, and the read function allows you to write 17 (0x11) bytes in length, hence the one-byte overflow. It is the only buffer on the stack, so behind it has to be the EBP, the only thing I can overflow the buffer to write into. Again, I was thinking to myself: How can I possibly change the EBP so that I can call the win function? I did notice that the memory address of init() was leaked, so then I could calculate the memory address of the win() function, and I kept this in the back of my head as I went on.

From here, I began to Google, and I found a few articles that helped me, one being [this one](https://www.exploit-db.com/docs/english/28478-linux-off-by-one-vulnerabilities.pdf). This particular one-byte overflow vulnerability is technically named the "Off-by-One Overflow", and the way to exploit this is to overwrite the least significant byte of the EBP since the binary is coded in little-endian (you can check it by trunning the Linux file command), so that it will point to another stack address. What also happens is that since the EBP is pointing to a different address after the overflow, the return address also changes, as it's placed after the location of the RBP. So, the idea of my exploit is that I need to find a region in the stack memory where I can get the RBP to point to with the Off-by-One Overflow so that return address is changed into the win() function, which initially was at the start of my payload followed filler bytes and then the one byte that would overflow the buffer.

According to the articles I read up on, challenge solvers were able to use GDB to find what byte to set the least significant byte to in the RBP for the exploit to work, but when I tried what they did, I found that it didn't work. My next realization was that the binary provided implemented the **P**osition-**I**ndependent **E**xecutable (**PIE**) mechanism. What the mechnism does is that the memory addresses of the stack and instructions are always randomized so that the relative offets between some addresses were not so predictable. Therefore, when I tried to use the same byte to overwrite the least significant byte in the RBP, it wouldn't work. What I ended up figuring out is that this exploit would be a hit-or-miss: sometimes it would work, sometimes not, depending on the randomized state of the memory the program is loaded on. So, I had the script run multiple times and had the win() address written in the payload as many times as I could in the buffer (4 times) to increase the likelihood of the win() address becoming the return address. With that, I finally cracked the challenge and got the flag with the spawned shell from win().

####Flag: DUCTF{all_1t_t4k3s_is_0n3!}

Solved by giggsterpuku