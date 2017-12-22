# -*- coding: utf-8 -*-
a=[]
b=[]
n=int(input('Digite a quantidade de elementos de a: '))
m=int(input('Digite a quantidade de elementos de b: '))
for i in range(n):
    a.append(int(input('Digite o elementoa: ')))
for j in range(m):
    b.append(int(input('Digite o elementob: ')))
soma=0
for w in range(n):
    for k in range (m):
        if b in a:
            soma=+1
print (soma)