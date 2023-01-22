#!/usr/bin/env python3

from pwn import *
from Crypto.Cipher import DES
import binascii
from tqdm import tqdm

def pad(msg):
  block_len = 8
  over = len(msg) % block_len
  pad = block_len - over
  return (msg + " " * pad).encode()

def double_encrypt(m, KEY1, KEY2): # for brute force
  msg = pad(m)
  cipher1 = DES.new(KEY1, DES.MODE_ECB)
  enc_msg = cipher1.encrypt(msg)
  cipher2 = DES.new(KEY2, DES.MODE_ECB)
  return binascii.hexlify(cipher2.encrypt(enc_msg)).decode()

def double_decrypt(m, KEY1, KEY2):
  msg = m
  cipher2 = DES.new(KEY2, DES.MODE_ECB)
  enc_msg = cipher2.decrypt(msg)
  cipher1 = DES.new(KEY1, DES.MODE_ECB)
  return cipher1.decrypt(enc_msg)

def get_key(val, dict):
  for key, value in dict.items():
    if val == value:
      return key
  return "No key"

p = remote("mercury.picoctf.net", 1903)
p.recvuntil("Here is the flag:\n")
enc_flag = p.recvline().strip()
p.sendlineafter("What data would you like to encrypt?", "69")
enc_test = p.recvline().strip()
p.close()
#print(enc_flag, enc_test)
log.info(f"Encrypted Flag: {enc_flag} Encrypted Test String: {enc_test}")

test = pad(binascii.unhexlify("69").decode())
#print(test)
part_enc_test = dict()

log.info("Making single DES encryption dictionary")
for i in tqdm(range(1000000)):
  key1 = bytes("0" * (6 - len(str(i))) + str(i) + " " * 2, 'utf-8')
  cipher1 = DES.new(key1, DES.MODE_ECB)
  part_enc_test[cipher1.encrypt(test)] = key1 #part_enc_test[key1] = cipher1.encrypt(test) also works, but this makes the search in the 2nd for loop much faster
  #print(key1, part_enc_test[key1])

log.info("Checking for matching decryptions in dicionary")
for i in tqdm(range(1000000)):
  key2 = bytes("0" * (6 - len(str(i))) + str(i) + " " * 2, 'utf-8')
  cipher2 = DES.new(key2, DES.MODE_ECB)
  part_dec_test = cipher2.decrypt(binascii.unhexlify(enc_test))
  #print(key2, part_dec_test)
  if part_dec_test in part_enc_test:
    key1 = part_enc_test[part_dec_test]
    print(f"First Key: {key1}\nSecond Key: {key2}")
    flag = double_decrypt(binascii.unhexlify(enc_flag), key1, key2)
    print(flag)

'''
# This just pure brute force, which will take massive amounts of time. However, we don't need to do that thanks to a MITM attack.
for i in range(1000000):
  for j in range(1000000):
    key1 = bytes("0" * (6 - len(str(i))) + str(i) + " " * 2, 'utf-8')
    key2 = bytes("0" * (6 - len(str(j))) + str(j) + " " * 2, 'utf-8')
    #print(key1, key2)
    res = double_encrypt(test, key1, key2)
    #print(type(res))
    if res == enc_test:
      print(f"First Key: {key1}\nSecond Key: {key2}")
      flag = double_encrypt(enc_flag, key1, key2)
      print(flag)
      break
'''
