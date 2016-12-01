# -*- coding: utf-8 -*-
from __future__ import division
n=input('Digite a quantidade de salas:')
a=[]
for i in range(0,n,1):
    a.append(input('Digite um elemento:'))

entrada=input('Digite a porta de entrada:')
saida=input('Digite a porta de saida:')

soma=0
while saida>=entrada:
    soma=soma+a[saida]
    saida=saida-1

print(soma)
