## Challenge: Ready Gladiator 0

## Category: Reverse Engineering

## Description: Can you make a CoreWars warrior that always loses, no ties? Your opponent is the Imp. The source is available here.

### Hints:

#### 1. CoreWars is a well-established game with a lot of docs and strategy

#### 2. Experiment with input to the CoreWars handler or create a self-defeating bot

Gist: Run a NOP instruction to do basically nothing to easily terminate your process. The Imp will continue to run due to its MOV instruction, allowing it to win all trials.

### Flag: picoCTF{h3r0_t0_z3r0_4m1r1gh7_e476d4cf}

Solved by giggsterpuku
