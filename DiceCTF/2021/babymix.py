#!/usr/bin/env python3

import angr, claripy

################################# Write-Up ####################################
# CTF: DiceCTF 2021
# Category: rev
# Challenge: babymix
# Points: 110 (after comp)
# Description: Just the right mix of characters will lead you to the flag :)
#
# Unpacking the binary in Ghidra, I found that the program uses a butt ton of
# checks w/ math comparisons to check your input. I figured that it would take
# too much time figuring out what characters are in the flag from the checks,
# so automated reversing is the way. I should probably continue looking into
# z3-solver and angr, but I used a script from a write-up to try this out and
# learn from it.
#
# Note: The script was taken from this Github write-up:
# https://github.com/WastefulNick/CTF-Writeups/tree/master/DiceCTF/reversing/babymix
#
# Flag: dice{m1x_it_4ll_t0geth3r!1!}
#
# Solved by: Ryan Nguyen
###############################################################################

# Import babymix binary for analysis
proj = angr.Project('./babymix')

#From looking at the decompiled math comparisons/checks in Ghidra, there are 22 characters compared in the desired output.
inp_len = 22

# Angr's Claripy module works with bitvectors (data in stings of bits). 2nd arg specifies how many bits it shoudl work with to get the flag.
stdin = claripy.BVS('flag', 8 * inp_len)

# When the program is run by this script, Angr will analyze its running state (conditions) through standard input.
state = proj.factory.entry_state(stdin=stdin)

# Constrains on the characters in the solution: must be a printable character
for i in range(inp_len):
	state.solver.add(stdin.get_byte(i) >= 33) # 33 in ASCII is !
	state.solver.add(stdin.get_byte(i) <= 126) # 126 in ASCII is ~

# The SimulationManager of Angr performs symbolic execution (analyzing the binary at defferent states when it runs)
simgr = proj.factory.simulation_manager(state)

# When the solution is found, this will print out the word "Correct"
simgr.explore(find=lambda s: b'Correct' in s.posix.dumps(1))

print(simgr.found[0].posix.dumps(0).decode())
print(simgr.found[0].posix.dumps(1).decode())
