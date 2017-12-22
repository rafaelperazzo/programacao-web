# -*- coding: utf-8 -*-
j = int(input('Digite a quantidade de numeros: '))
n = []
p = []
m = []
for i in range(j):
    n.append(int(input('Digite os numeros: '))) 
for i in range(n):    
    if i % 2==0:
        p.append(i)
    else:
        m.append(i)
print(n)
print(p)
print(m)
    