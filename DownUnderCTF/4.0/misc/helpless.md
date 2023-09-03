### Challenge: helpless

#### Category: misc 

#### Description: I accidentally set my system shell to the Python help() function! Help!! The flag is at /home/ductf/flag.txt.

#### Author: hashkitten

I have to thank Pix for really helping me out in figuring out the exploit in the challenge with 15 minutes left in the CTF (I pretty much felt I was spoonfed the answer, but he/she was really nice about helping me approach this challenge the right way). Logging onto the SSH server where the challenge was hosted, I found that I was launched into the interactive help command prompt of Python. I first approached this challenge as a pyjail, so I tried finding maybe some modules to maybe be able to use for code execution, but of course that wouldn't work as whatever I typed seemed to always be interpreted as a search string. There was no way to escape the prompt, as typing quit, would just log you off the challenge server instead of getting into the interactive Python environemnt like it usually would.

Here's where Pix came to the rescue. He/she suggested I take notice of how the information is displayed in the interactive help when I search something up and see if I can somehow read files from it. I noticed that when I search for a module, say os, I read the help entry through a familiar prompt to me: the text editor less. From there, it clicked in my head that I was able to run less commands in the editor, like typing in "q" for exiting the editor. Pix suggested I read the man pages a bit, so I did and found that I could read/edit another file by typing in ":e \[filename\]". With that, I typed in ":e /home/ductf/flag.txt" and boom, flag found.

#### Flag: DUCTF{sometimes_less_is_more}

Solved by giggsterpuku
