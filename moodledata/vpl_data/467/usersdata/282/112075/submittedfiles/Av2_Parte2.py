# -*- coding: utf-8 -*-
#listas a e b
n=int(input('Digite a quantidade de elementos da lista a: '))
m=int(input('Digite a quantidade de elementos da lista b: '))
a=[]
for i in range(0,n):
    a.append(int(input('Digite os elementos da lista a: ')))
b=[]
for i in range(0,m):
    b.append(int(input('Digite os elementos da lista b: ')))
    
print(a)
print(b)

#quantidade de elementos de a em b
quant_a_em_b=[]
cont=0
for i in range(0,b,1):
    cont += i
    quant_a_em_b.append(cont)
    
print(quant_a_em_b)
    