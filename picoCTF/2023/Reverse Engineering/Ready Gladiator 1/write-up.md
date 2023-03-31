##Challenge: Ready Gladiator 1

##Category: Reverse Engineering

##Description: Can you make a CoreWars warrior that wins? Your opponent is the Imp. The source is available here. If you wanted to pit the Imp against himself, you could download the Imp and connect to the CoreWars server like this: nc saturn.picoctf.net 57700 < imp.red. To get the flag, you must beat the Imp at least once out of the many rounds.


### Hints:

####1. You may be able to find a viable warrior in beginner docs

Looking at [this document](https://vyznev.net/corewar/guide.html#introduction) that I used to fir understand CoreWars in the previous challenge Ready Gladiator 0, the warrior that I implemented was the Dwarf. Essentially what the Dwarf does is plant a DAT instrutction that it leaves for its opponent to hit what it is the opponent's turn, thus terminating its program. The Dwarf will keep itself running (on the assumption that the opponent does not tamper its code, which is a strong possibility) by looping in its instructions. Regardless, I input the Dwarf's code to the remote sever, and it won a few times, getting the flag.

### Flag: picoCTF{1mp_1n_7h3_cr055h41r5_b182a3f1}

Solved by giggsterpuku
