# -*- coding: utf-8 -*-
from __future__ import division

def pico(lista):
    cont=0
    for i in range(0,len(lista),1):
        if lista[i-1]<lista[i]>lista[i+1]:
            cont+=1
        elif lista[i-1]>lista[i]<lista[i+1]:
            lista[i-1]=lista[i]
            lista[i]=lista[i+1]
    if cont==1:
        return True
    else:
        return False
#Entrada
a=[]
n=int(input('digite n:'))
#processamento
for i in range(0,n,1):
    a.append(input('digite um elemento:'))
pico_a=pico(a)    
#saida
if pico(a):
    print('S')
else:
    print('N')
    