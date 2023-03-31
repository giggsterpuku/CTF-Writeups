## Challenge: Virtual Machine 0

## Category: Reverse Engineering

### Description: Can you crack this black box? We grabbed this design doc from enemy servers: Download. We know that the rotation of the red axle is input and the rotation of the blue axle is output. The following input gives the flag as output: Download.

### Hints:

#### 1. Rotating the axle that number of times is obviously not feasible. Can you model the mathematical relationship between red and blue?

This chall ended up being way easier than I thought at first. Looking at the file from the "enemy servers," it looks like a 3D model. Opening it up on an online DAE viewer, it looks to be a Lego model of some black box with a red and blue rod sticking out of it like what the description describes.

![https://github.com/giggsterpuku/CTF-Writeups/blob/main/picoCTF/2023/Reverse%20Engineering/Virtual%20Machine%200/gears.png]

However, when you take away all the black bricks in the model, what remains are the rods and the gears that move if you were to move the red rod to move the blue one. The red gear looks to be a 40-tooth gear, and there are 2 8-tooth gears subsequently in contact, creating a 3-gear ger train. Taking up the hint, I realize that the gear ration is 40:8, or 5:1, so that means that for every rotation of the red rod/red gear, the blue gear rotates 5 times. That means that for the number that the number of rotations that I input, the blue rod with rotate 5 times more. The solution was to multiply the long number input by and convert it to bytes to get the flag. I didn't read the instruction properly, so I interpreted the input number as a list of multiple single numbers, so I thought I had to rotate the red gear bu each number and find the character it mapped to each time, but that did not end up being the case. Whatever though, I was able to figure out I goofed so all is fine. :)

###Flag: picoCTF{g34r5_0f_m0r3_cef8e141}

Solved by giggsterpuku
