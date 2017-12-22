# -*- coding: utf-8 -*-

def elementos (c):
    x = 0
    for i in range (0,c,1):
        if i in a1:
            if i in b1:
                x += 1
    return x

a = int(input())
b = int(input())
a1 = []

for i in range (0,a,1):
    a1.append(str(input()))
b1 = []
for i in range (0,b,1):
    b1.append(str(input()))

print(elementos(a))