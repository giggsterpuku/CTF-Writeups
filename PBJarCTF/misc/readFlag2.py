#!/usr/bin/env python3

################################## Write-Up ####################################
# Challenge: readFlag2
# Category: misc
# Description: I have republished the previous the contract at 0x585C403bC5c7eb62BF3630c7FeF1F837603bA866, but this time no source code for you this time. Luckily, the ABI of the smart contract is the same as the previous one. Figure out how to "get()" the flag. Important: This smart contract is on Ropsten
# Author: bruh.#0766
#
# This chall was very inciteful, and I learned a lot about how Ethereum
# cryptocurrency works through it. The goal of this chall was to call the get()
# function of the smart contract. At first I though this was rev and decompiled
# the bytecode (it's Solidity), but it was all gobbledygook. I didn't need to do
# that ;-;. So, I read some articles on making transactions and interacting with
# smart contracts, and I found that one way to do those is to use a JS/Python
# module called web3 (traditionally JS is used, but Python later implemented it)
# I used this guide to make this script and get the flag:
# https://www.dappuniversity.com/articles/web3-py-intro
#
# Flag: flag{web3js_plus_ABI_equalls_flag}
# Points: 248 (at time of solve)
# Solved by: Ryan Nguyen
# Solved at: 30 hrs into comp
################################################################################

import json
from web3 import Web3

infura_url = "https://ropsten.infura.io/v3/1cd3c16336df44d38c09f96b95558c5a"
web3 = Web3(Web3.HTTPProvider(infura_url))
address = "0x585C403bC5c7eb62BF3630c7FeF1F837603bA866"
abi = json.loads('[{"inputs":[],"name":"get","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"}]')
contract = web3.eth.contract(address=address, abi=abi)
#print(web3.isConnected())
#print(web3.eth.blockNumber)
print(contract.functions.get().call())
