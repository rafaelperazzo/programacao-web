# -*- coding: utf-8 -*-
j = int(input('Digite a quantidade de numeros: '))
n = []
p = []
m = []
for i in range(j):
    n.append(int(input('Digite os numeros: '))) 
for c in range(n[0], n[j-1], n[j]):
    if c % 2 == 0:    
        p.append(c)
print(n)
print(p)
