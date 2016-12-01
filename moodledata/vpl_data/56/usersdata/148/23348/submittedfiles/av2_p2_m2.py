# -*- coding: utf-8 -*-
from __future__ import division
n=input('Digite a quantidade de salas:')
a=[]
for i in range(0,n,1):
    a.append(input('Digite um elemento:'))

entrada=input('Digite a porta de entrada:')
saida=input('Digite a porta de saida:')

vida=0
for i in range(entrada,saida+1,1):
    vida=vida+a[entrada]

print(vida)
