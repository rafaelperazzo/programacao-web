# -*- coding: utf-8 -*-
'''
def elementos (c):
    x = 0
    for i in range (0,k,1):
        if i in a:
            if i in b:
                x += 1
    return x
'''
k = 1000000
a = int(input())
b = int(input())
a1 = []

for i in range (0,a,1):
    a1.append(int(input()))
b1 = []
for i in range (0,b,1):
    b1.append(int(input()))

x = 0
for i in range (0,k,1):
    if i in a:
        if i in b:
            x += 1

print(x)