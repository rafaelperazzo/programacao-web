# -*- coding: utf-8 -*-
'''
def elementos (c):
    x = 0
    for i in range (0,k,1):
        if [i] in a1:
            if [i] in b1:
                x += 1
    return x
'''
    
    
def elementos (c):
    x = 0
    if a1[0] in b1:
        x += 1
    if a1[1] in b1:
        x += 1
    if a1[2] in b1:
        x += 1
    if a1[3] in b1:
        x += 1
    if a1[4] in b1:
        x += 1
    if a1[5] in b1:
        x += 1
    if a1[6] in b1:
        x += 1
    if a1[7] in b1:
        x += 1
    if a1[8] in b1:
        x += 1
    if a1[9] in b1:
        x += 1
    if a1[10] in b1:
        x += 1
    if a1[11] in b1:
        x += 1
    if a1[12] in b1:
        x += 1
    if a1[13] in b1:
        x += 1
    if a1[14] in b1:
        x += 1
    if a1[15] in b1:
        x += 1
    return x

k = 1000000
a = int(input())
b = int(input())
a1 = []
for i in range (0,a,1):
    a1.append(int(input()))
b1 = []
for i in range (0,b,1):
    b1.append(int(input()))

print(elementos(a))














