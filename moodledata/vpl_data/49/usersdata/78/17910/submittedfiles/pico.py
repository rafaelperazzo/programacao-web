# -*- coding: utf-8 -*-
from __future__ import division


def pico(lista):
    posição=0
    for i in range(0,len(lista),1):
        if lista[i]<lista[i+1]:
            posição=i
            if lista[i-1]<lista[i]>lista[i+1]:
                return True
            else:
                return False
    


n = input('Digite a quantidade de elementos da lista: ')
a=[]

for i in range(0,n,1):
    a.append(input('digite o elemento da lista:'))
    
if pico(a)==True:
    print('S')
else:
    print('N')
