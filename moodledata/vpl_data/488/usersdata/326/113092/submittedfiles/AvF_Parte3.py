# -*- coding: utf-8 -*-
j = int(input('Digite a quantidade de numeros: '))
n = []
p = []
m = []
for i in range(j):
    n.append(int(input('Digite os numeros: '))) 
import split 
for c in range(n):
    if c % 2 == 0:    
        p.append(c)
    else:
        m.append(c)
print(n)
print(p)
print(m)
