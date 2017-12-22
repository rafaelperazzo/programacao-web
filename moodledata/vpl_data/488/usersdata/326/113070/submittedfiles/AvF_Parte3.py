# -*- coding: utf-8 -*-
j = int(input('Digite a quantidade de numeros: '))
n = []
p = []
m = []
for i in range(j):
    n.append(int(input('Digite os numeros: '))) 
for n in range(n[0], n[j-1]):
    if n % 2 == 0:    
        p.append(n)
    else:
        m.append(n)
print(n)
print(p)
print(m)
