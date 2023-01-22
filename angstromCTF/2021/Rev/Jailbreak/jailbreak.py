#!/usr/bin/env python3

################################## Write-Up ####################################
# Challenge: Jailbreak
# Category: Rev
# Points: 75
# Description: Clam was arguing with kmh about whether including 20 pyjails in a ctf is really a good idea, and kmh got fed up and locked clam in a jail with a python! Can you help clam escape? Find it on the shell server at /problems/2021/jailbreak over over netcat at nc shell.actf.co 21701.
# Author: aplet123
#
# So to explain how to solve the chall I will split my explanation into 3
# steps. The first is to "escape the jail." Running the binary the first time,
# the program seems to make a loop when you input stuff. However, I ran ltrace
# and found that my input was compared to several strings, and if your input
# does not match, the program loops.From running the strings fished out by
# ltrace, I figured the program was an adventure-type thing, as you are trapped
# in a cell with a snake while kmh stares at you (wooooo). So, the way to get
# out (after trial and error of putting in valid inputs) was to "pick the snake
# up", "throw it at kmh" to make him flee, and "pry the bars of the cell open."
# Once you "escape" and "look around," you see that there are 2 buttons to push:
# one red, one green. At first, I just "pressed" them, and it seemed "nothing
# happens." However, I decided to do some static analysis and look at it in
# Ghidra. The functions had a lot of math going on, but I was able to figure
# out the flow and see how step 1 led to step 2 as in what conditions led up
# to opening the file. The 2nd step had to do with satisfying this asm
# instruction: cmp r12, 0x539. I figured that "pressing" the buttons affected
# this, so I went to GDB to monitor the changes of r12 when I "pressed" the
# buttons. After trial and error, I figured that r12 started at 1 when I
# "escaped," and that pressing a button would tack on a 0 (if red) or 1 (if
# green) to the end of it as if it was a binary number, and that value would be
# compared to 0x539. The solution was to then press the buttons in an order that
# would make the binary string 0x539, so I got the binary conversion of 0x539
# and figured the order to press the buttons. Now the 3rd step: "get out."
# Once again, I ran ltrace to see if there were any options left to type other
# than "press the * button" since the output still said "nothing happened."
# "bananarama" was the new option, and I typed it to solve the challenge and
# (hypothetically) get the flag.
#
# Flag: <server removed and post-CTF, no none at the time of solve>
# Solved by: Ryan Nguyen
# Solved on: 9/1/2021


from pwn import *

exe = ELF("jailbreak")

context.binary = exe

red = "press the red button"
green = "press the green button"

def main():
	r = process([exe.path])
	r.sendlineafter("What would you like to do?", 'pick the snake up')
	r.sendlineafter("What would you like to do?", 'throw the snake at kmh')
	r.sendlineafter("What would you like to do?", 'pry the bars open')
	button_mash = [red, green, red, red, green, green, green, red, red, green]
	for i in button_mash:
		r.sendlineafter("What would you like to do?", i)
	r.sendlineafter("What would you like to do?", 'bananarama')
	r.interactive()

if __name__ == "__main__":
	main()
