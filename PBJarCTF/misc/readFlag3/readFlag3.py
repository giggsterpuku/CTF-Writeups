#!/usr/bin/env python3

################################## Write-Up ####################################
# Challenge: readFlag3
# Category: misc
# Description: 0xe2a9e67bdA26Dd48c8312ea1FE6a7C111e5D7a7A. Important: This smart contract is on Ropsten
# Author: bruh.#0766
#
# The main gist of this chall is to send the smart contract request as the
# accounht owner. There was an owner() function, so I used it to get the address
# of the owner, and using the web3.eth.defaultAccount property from web3, I was
# able to get the flag as intended.
#
# Flag: flag{s3t_by_c0nstructor}
# Points: 205 (at time of solve)
# Solved by: Ryan Nguyen
# Solved at: 31 hrs into comp
################################################################################

import json
from web3 import Web3

infura_url = "https://ropsten.infura.io/v3/1cd3c16336df44d38c09f96b95558c5a"
web3 = Web3(Web3.HTTPProvider(infura_url))
address = "0xe2a9e67bdA26Dd48c8312ea1FE6a7C111e5D7a7A"
abi = json.loads('[{"inputs":[{"internalType":"string","name":"_flagVal","type":"string"}],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[],"name":"get","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"}]')
web3.eth.defaultAccount = "0x2fB392F144b8e02e422a817437d293d9f2b9Dee8"
contract = web3.eth.contract(address=address, abi=abi)
#print(web3.isConnected())
#print(web3.eth.blockNumber)
#print(contract.functions.owner().call()) -> got owner address
print(contract.functions.get().call())
