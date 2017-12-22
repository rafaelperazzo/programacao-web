# -*- coding: utf-8 -*-
n = int(input('Digite a quant de elemntos: '))
lista = []
for i in range(n):
    lista.append(int(input()))
p = 0
for i in range(n-1):
    if i >=1 and i <= n-2:
        if lista[i+1] > lista[i] and lista[i+1] > lista[i+2]:
            p = p+1
if p == 1:
    print('S')
else:
    print('N')
    

