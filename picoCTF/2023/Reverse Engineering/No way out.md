## Challenge: No way out

## Category: Reverse Engineering

### Description: Put this flag in standard picoCTF format before submitting. If the flag was h1_1m_7h3_f14g submit picoCTF{h1_1m_7h3_f14g} to the platform.

Looking at the challenge, it seems that the provided zip file contains a Unity game. From my experience, the idea is to reverse engineer it using ILSpy and see how the program works. But first, I opened the pico.exe executable to see what the mechanics of the game were. I found that the goal is to escape a small closed boundary of what seems to be impassable wall that is of a finite height. You can move around with the WASD keys, jump with the space bar, crouch with the Ctrl key, and a couple more things. Looking into ILSpy and decompiling the Assembly-CSharp.dll file, I found that there was a lot of gunk to filter, and I found the important stuff to be in the PlayerController object code, which shows the actions that you can do with the keyboard that correlate to those described in the game by the menu. Each action listed in PlayerController() seems to be correlated to a dictionary labeled KeyCode by the way. In order to escape the small walled-up area in the game, I figured that one way was to try to jump over the wall high enough to not get blocked by the wall. So, I thought of patching the Assembly-CSharp.dll file so that the jumping ability is magnified. Looking at the PlayerController() code, I editted the following section of code:

```c++
			if (Input.GetButton("Jump") && this.canMove && this.characterController.isGrounded && !this.isClimbing)
			{
				this.moveDirection.y = 25f; // this was originally set to this.jumpingSpeed. I initially tried to edit this.jumpingSpeed to reflect a high number, but by testing it I realized it did not work, so I ended up changing this variable directly.
			}
```

After making the patch, I restrated the game. I was able to jump over the wall, and BOOM, I got the flag.

### Flag: picoCTF{WELCOME_TO_UNITY!!}

Solved by giggsterpuku
