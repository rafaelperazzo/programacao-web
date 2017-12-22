# -*- coding: utf-8 -*-
n=int(input('Digite a quantidade de elementos da lista a: '))
a=[]
for i in range(0,n):
    a.append(int(input('Digite os elementos da lista: ')))
a.append(a)
print(a)

    