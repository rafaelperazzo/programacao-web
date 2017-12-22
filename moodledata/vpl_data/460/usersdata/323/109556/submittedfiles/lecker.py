# -*- coding: utf-8 -*-
a=[]
b=[]
n=int(input('Digite a quantidade de elementos da lista: '))

for i in range(0,n,1):
    valor_a=float(input('Digite o elemento da lista: '))
    a.append(valor_a)
for i in range(0,n,1):
    valor_b=float(input('Digite o elemento da lista: '))
    b.append(valor_b)
for i in range(0,n,1):
    cont=0
    if a.index(max(a)) > a[i]:
        print('S')
    else:
        print('N')