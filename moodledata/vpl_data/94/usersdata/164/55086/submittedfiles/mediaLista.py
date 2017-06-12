# -*- coding: utf-8 -*-
n=int(input('Digite a quantidade de elementos da lista: '))
a=[]
soma=0
for i in range (1, n+1, 1):
    valor=int(input('Digite os valores da lista: '))
    a.append(valor)
for j in range (0, len(a), 1):
    soma=soma+a[j]
media=soma/len(a)
print(a[0])
print(a[len(a)-1])
print(media)
print(a)
