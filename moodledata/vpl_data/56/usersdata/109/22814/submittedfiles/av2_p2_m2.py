# -*- coding: utf-8 -*-
from __future__ import division

n=input('Digite a quantidade de salas:')
a=[]

for i in range (0,n,1):
    a.append(input('Digite a quantidade de vidas da sala:'))
    
b=input('Digite a porta de entrada:')
c=input('Digite a porta de saída:')

cont=0
for i in range(b-1,c,1):
    cont=cont+(a[i])
    
print cont