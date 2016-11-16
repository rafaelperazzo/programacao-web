# -*- coding: utf-8 -*-
from __future__ import division

def pico(lista):
#CONTINUE...
    indice=0
    for i in range(0,len(lista),1):
        if lista[i]>lista[i+1]:
            indice=i
            break
    
    contador=0
    for i in range(indice, len(lista),1):
        if lista[i]<=lista[i+1]:
            contador=contador+1
    
    if contador==0 and indice!=0:
        return True
    
    else:
        return False


n = input('Digite a quantidade de elementos da lista: ')
#CONTINUE...
a=[]
for i in range(0,n,1):
    a.append(input('Digite os elementos de a: '))

if pico(a):
    print('S')

else:
    print('N')
