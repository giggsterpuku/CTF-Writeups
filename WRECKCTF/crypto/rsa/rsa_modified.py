#!/usr/bin/env python3

from Crypto.Util.number import *
p = getPrime(1024)
q = getPrime(1024)
n = p * q
e = 65537
flag = open('flag.txt', 'rb').read()
d = inverse(e, (p-1)*(q-1))

pandaman = b"PANDAMAN! I LOVE PANDAMAN! PANDAMAN MY BELOVED! PANDAMAN IS MY FAVORITE PERSON IN THE WHOLE WORLD! PANDAMAN!!!!"

def enc(m):
    if pandaman == m:
        return "No :("
    else:
        return pow(m, d, n)

def check(c):
    if long_to_bytes(pow(c, e, n)) == pandaman:
        print(flag)
    else:
        print("darn :(")

def menu():
    print("1. Encrypt")
    print("2. Check")
    print("3. Exit")

def main(choice,input):
    menu()
    if choice == "1":
        ans = enc(input)
        print(ans)
        return ans
    elif choice == "2":
        check(input)
    elif choice == "3":
        exit()
    else:
        print("Invalid choice")


m1 =  5 * 7 * 127 * 193 * 21211 * 254447 * 72050257
m2 = 1939303315420219046960018154685373915387234571881073610300392793536129074899070311578399989850647897594894191349572540907622153300914865620787414911914481665252463115484878819316899244103608295017235223309381353356534696286848452920032763470993
c1 = main("1", m1)
c2 = main("1", m2)
main("2", c1*c2)
