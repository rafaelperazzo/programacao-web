# -*- coding: utf-8 -*-
from __future__ import division

def pico(lista):
    for i in range(0,len(lista)-1,1):
        if lista[i]>lista[i+1]:
            posi=i
            break
       
    c=0
    for i in range(posi,len(lista)-1,1):
        if a[i]<=a[i+1]:
            c=c+1
    if c==0 and posi!=0:
        return True
    else:
        return False
            
n = input('Digite a quantidade de elementos da lista: ')
a=[]
for i in range(0,n,1):
    a.append(input('digite os termos:'))

if pico(a):
    print('S')
else:
    print('N')
    
