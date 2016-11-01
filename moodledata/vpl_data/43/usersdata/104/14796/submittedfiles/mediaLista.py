# -*- coding: utf-8 -*-
from __future__ import division
#Entrada
n=input('Digite o valor de n:')
l=[]
soma=0
#Processamento
for i in range(0,n,1):
    l.append(input('Digite o valor:'))
for i in range(0,n,1):
    soma=soma+l[i]
#Saída
print('%.2f'%(l[0]))
print('%.2f'%(l[i]))
print('%.2f'%(soma/len(l)))
print(l)

