# -*- coding: utf-8 -*-
from __future__ import division


def lecker(lista):
    for i in range:
        if i==0:
            if lista[i]>lista[i-1]:
                contador=contador+1
        elif i==len(lista)-1:
            if lista[len(lista)-1]>lista[len(lista)-2]:
                contador=contador+1
    if contador==1:
        return true
    else:
         return false

n=input('Digite o total de valores de ambas as lista:')

hannibal=[]
freddy=[]

for i in range(0,n,1):
    hannibal.append(input('Acrescente o número de vítimas a hannibal:'))
    
for i in range(0,n,1):
    freddy.append(input('Acrescente o número de vítimas a freddy:'))
    
if lecker(hannibal):
    print('S')
else:
    print('N')
if lecker(freddy):
    print('S')
else:
    print('N')
    

