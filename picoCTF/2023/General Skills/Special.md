##Challenge: Special

##Category: General Skills

##Description: Don't power users get tired of making spelling mistakes in the shell? Not anymore! Enter Special, the Spell Checked Interface for Affecting Linux. Now, every word is properly spelled and capitalized... automatically and behind-the-scenes! Be the first to test Special in beta, and feel free to tell us all about how Special streamlines every development process that you face. When your co-workers see your amazing shell interface, just tell them: That's Special (TM)

###Hints:

####1. Experiment with different shell syntax

Logging onto the server, I tried so many BASH commands, but all of them were tranlated into some grammaticized English words, and they were input as commands into SH, which it did not understand. In addition, I was not allowed to invoke another shell by typing its name into the terminal like one usually does. I tried to find a way to bypass the mechanism, and I found that if I used relative addressing to refer to the BASH executables in /bin (e.g. ../../../../../bin/ls), and I used them to ls and cat my way to the flag. ls showed that a directory named blargh had the flag.txt file, and I cat'd the flag out. Since I couldn't type in the file names correctly, I used the wildcard character (*) to refer to the files.

###Flag: picoCTF{5p311ch3ck_15_7h3_w0r57_a60bdf40}

Solved by giggsterpuku
