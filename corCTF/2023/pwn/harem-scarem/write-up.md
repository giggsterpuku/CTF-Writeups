###Challenge: harem-scarem

#####Category: pwn

#####Description: Another year, another quirky language to pwn

####Introduction

Just a disclaimer: I did not solve this challenge durign the CTF. I reviewed this challenge to learn for future CTFs. Initially, there was no write-up for this challenge posted on the CTF Discord server, but the closest thing I had to it was someone by the username of Shunt saying:

>>> *"Out of bound read write then rop"*

In addition, I looked on CTFTime to see if any write-ups for this challenge was posted there. Unfortunately, there wasn't but I got a hint on how to solve this challenge from the "sigrop" category label on it. Thus, I guessed that **S**ig**r**eturn-**O**riented **P**rogramming (a.k.a. **SROP**) would be the technique to get the flag here. With these pieces of intel in mind, I started the challenge.

####Background Information

I'd say before I jump into how I solved the challenge, I think looking up and knowing how to perform **R**eturn-**Oriented** **P**rogramming (**ROP**) and buffer overflows would be important for explaining what SROP is, so look up some CTF write-ups/articles on those!

Essentially, from what I learned to solve this challenge, SROP is using a particular system call (a.k.a. syscall) to perform program execution on the assumption that you can overwrite the instruction pointer (a.k.a. RIP/EIP) in a program's memory. How it works is that some simple gadgets will need to be used to 1) set the RAX register to 15, and 2) invoke the syscall assembly instruction. From there, the rt_sigreturn() system function is called, invoking the system's signal handler. A lot of junk is moved around and registers are being changed up as the signal handler does its work, so a special context/stack frame (a.k.a. sigreturn frame) set up to store the values of the registers in the program's state before the signal handler was invoked. That way, when the handler is done, the program can resume from where it left off. Now, a program user can exploit this behavior by using the aforementioned simple gadgets into a payload to perform a buffer overflow/RIP overwrite and tacking on a forged sigreturn frame that the program's handler will return to change the values of the registers as the user so desires.

####Finding the exploit

My first instinct was to look at the source code first and play around with the program so see how it worked. The "quirky language" that I've come to recognize and learn about from this challenge is Hare. For sake of checking any binary exploitation counternmeasures, I ran checksec and found no protections on the binary at all, so a lot of exploits seemed to be fair game at first. From quick observations on  the program, the program gives you some memory to deal with to make 8 notes: each one has 32 bytes of memory for a title, 128 bytes for some note content, and 1 byte for a boolean value for the program to check if a note at given location in the notes array is written in or not.

It took me a day or two to figure out the fishy lines of code that could be exploited. I first found this check in the ptr_back() function to be interesting:

```hare
fn ptr_back(p: *u8) void = {
    if (*p - 1 < 0) {
        fmt::println("error: out of bounds seek")!;
    } else {
        *p -= 1;
    };
    return;
};
```

If you can read the Hare code, you may observe that the input pointer that is checked contains an unsigned 8-bit value. Because the value is unsigned **it can never be negative**. Thus, this check can be bypassed, as subtracting 1 from the pointer value when the value of the pointer is 0 will create an integer underflow and result in 255 as its value (and this was verified by my experiments in GDB). This allows for the "Out of bound read write" that can be performed, as you now have access to higher addresses beyond the notes array in memory. This vulnerability, along with the note_add() and note_read() commands, create read and write primitives to be used (see the source code if you want more detail on how note_add() and note_read() work, but their functions should be intuitive from how they're named).

####The exploit

At this point, I was ready to make a solve script. However, this took the longest time, as I've never done an SROP exploit in a CTF challenge before. I was eventually able to make the script work, but first I had to overcome some hurdles:

1. I did not know what syscall to make to get the flag. I figured the way I've always known was to pop open a shell, so I figured calling ```c execve("/bin/sh", NULL, NULL)``` would be my way to go. For that, I would have to set RAX to 59, RDI to a pointer to a "/bin/sh" string, RSI and RDX to NULL (0), and the RIP to a syscall gadget.

2. To be able to run the function above, I needed a "/bin/sh" string to exist in memory. I figured the best place to write that was either going to be in the .bss section or a note where I know the location of. In the end, I went with the latter option, but to be able to do that...

3. I would have to know the location of the note to which I am writing to. In order to do that, I would have to perform a leak to read off a stack address and maybe perform some offset calculations to see where the note lies. From there, I would write in the address of the "/bin/sh" string to create a pointer and write in the "/bin/sh" string as well.

So, here is how I structured my solve script:

1. Take advantage of the pointer integer underflow and read off the RBP value. I calculated and verified in GDB where in the memory region where the RBP lied, and I found it to be at the theoretical 10th index of the 8-element-long notes array. From there, I calculated the difference in memory addresses the RBP was to the location of the note I was to write the "/bin/sh" string into, and then I calculated the address of the "/bin/sh" string. The reason why I calculated the address is to make the address of the first note the pointer to the string, so when I execute my payload with the address and the string inside, I know that when the execve() function runs and I supply the pointer's memory address to it, the "/bin/sh" string will be passed along successfully.

2. This is where SROP comes into play. To be able to change all the registers into the desired values to run ```c execve("/bin/sh", NULL, NULL)```, one or more gadgets will have to be chained to invoke the rt_sigreturn() system function. In the binary, there is a ```asm mov eax, 0xf; syscall``` gadget that does this all in one go, so I used it. So, the SROP payload looks like this: padding, then the gadget, and then the forged sigreturn frame with the desired register values. There was a hurdle inside of this, which was that the payload couldn not all be stuffed into a title/content buffer, so I had to split it up and write it into sequential and adjectent memory sections to make the payload work.

With all that and some head banging, I got the exploit to work. I learned a lot in this challenge, and it was really satisfying to go through the journey of solving it and eventually get the flag.

#####Flag: corctf{sur3ly_th15_t1m3_17_w1ll_k1ll_c!!}

Reviewed by giggsterpuku
