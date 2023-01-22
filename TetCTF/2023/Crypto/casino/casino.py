#!/usr/bin/env python3

from pwn import *
import json, base64

context.log_level = "DEBUG"

addr = "192.53.115.129"
port = 31338

r = remote(addr, port)
json_data=json.dumps({"recipient" : "Casino","command" : "Register","username" : "giggsterpuku"})
r.sendline(bytes(json_data, 'utf-8'))
r.recvline()
json_data=json.dumps({"recipient" : "Casino","command" : "Bet","username" : "giggsterpuku","amount" : -2**(8*40),"n" : 50}) # 8 for the number of bits in a byte (PrintFlag() counts the number of bytes), 40 for number of characters (flag didn't end up being that many)
r.sendline(bytes(json_data, 'utf-8'))
r.recvline()
json_data=json.dumps({"recipient" : "Casino","command" : "ShowBalanceWithProof","username" : "giggsterpuku"})
r.sendline(bytes(json_data, 'utf-8'))
msg = r.recvline().decode()[:-1].split(", ")[1]
print(msg) #print(base64.b64decode(msg))
json_data=json.dumps({"recipient" : "FlagSeller","command" : "PrintFlag","username" : "giggsterpuku","balance" : 2**320 + 2023,"proof_data" : str(msg)})
r.sendline(bytes(json_data, 'utf-8'))
r.recvline()
r.close()
