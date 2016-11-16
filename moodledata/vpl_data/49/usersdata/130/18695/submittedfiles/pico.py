# -*- coding: utf-8 -*-
from __future__ import division

def pico(lista):
    posicao=0
    for i in range(0,len(lista)-1,1):
        if lista[i]>lista[i+1]:
            posicao=i
        break
    cont=0
    for i in range(posicao,len(lista)-1,1):
       if lista[i]<=lista[i+1]:
           cont=cont+1
    if cont>=1:
        return False
    else:
        return True
    


n = input('Digite a quantidade de elementos da lista: ')
a=[]
for i in range(0,n,1):
    a.append(input('Digite um elemento:'))
if pico(a)==True:
    print('S')
else:
    print('N')
