#!/bin/python3
from pwn import *

'''
spits flag after 100 cycles
dawg ctf 2021 misc : Two Truths and a Fib
'''

def fib(n):
    c = 0
    a = 1
    b = 1
    if n == 0 or n == 1:
        return True
    else:
        while c < n:
            c = a + b
            b = a
            a = c
        if c == n:
            return True
        else:
            return False

r = remote("umbccd.io", 6000)
if __name__ == '__main__':

    for i in range(0,100,1):
        print ("current cycle: "+str(i+1))
        r.recvuntil("[")
        input = r.recvline().split()
        print (input)

        input[0] = input[0][:-1]
        input[1] = input[1][:-1]
        input[2] = input[2][:-1]

        for i in range (0,3):
            if fib(int(input[i])) == True:

                r.sendline(bytes(input[i]))
                print (">> "+str(input[i])+"\n")

            else:
                continue

    r.recvuntil("flag: ")
    print (r.recvline()[:-1])
