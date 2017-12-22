# -*- coding: utf-8 -*-
n = int(input())
lista = []
lista2 = []
for i in range(n):
    lista.append(int(input()))
p = 0
for i in range(n-1):
    if i >=1 and i <= n-2:
        if lista[i+1] > lista[i] and lista[i+1] > lista[i+2]:
            p = p+1
for i in range(n):
    lista2.append(int(input()))
p2 = 0
for i in range(n-1):
    if i > 0 :
        if lista2[i] > lista2[i+1] and lista2[i] > lista2[i-1]:
            p2 = p2+1
    if i == 0:    
        if lista2[i] > lista2[i+1]:
            p2 = p2+1
if p == 1:
    print('S')
else:
    print('N')
if p2 == 1:
    print('S')
else:
    print('N')
        

