# -*- coding: utf-8 -*-
from __future__ import division

n = int(input('insira a quantidade de salas:'))
a=[]

for i in range (0,n,1):
    a.append(input('insira a quantidade de vidas:'))
    
x=int(input('insira a porta de entrada:')) 
y=int(input('insira a porta de saída:'))

cont=0
for i in range(x,(y+1),1):
    cont=cont+a[i]


print cont 