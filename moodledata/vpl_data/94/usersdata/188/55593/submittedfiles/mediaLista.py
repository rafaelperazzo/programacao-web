# -*- coding: utf-8 -*-
n=int(input('Digite a quantidade de elementos da lista:'))
l=[]
soma=0
for i in range (0,n,1):
    o=float(input('Digite o valor de o:'))
    l.append(o)
soma=0
for i in range (0,len(l),1):
    soma=soma+l[i]
media=soma/len(l)
print('%.2f'%l[0])
print('%.2f'%l[len(l)-1])
print('%.2f'%media)
print(l)

