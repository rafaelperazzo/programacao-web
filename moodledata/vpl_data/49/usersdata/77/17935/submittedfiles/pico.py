# -*- coding: utf-8 -*-
from __future__ import division

def pico(lista):
    posição=0
    for i in range(0,len(a)-1,1):
        if a[i]>a[i-1]:
            posição=i
            break
    
    contador=0
    for i in range(0,len(a)-1,1):
        if a[i]<=a[i-1]:
            contador=contador-1
    
    
    if contador==0 and posição!=0:
        return True
    else:
        return False

a=[]
n = input('Digite a quantidade de elementos da lista: ')
for i in range(0,n,1):
    a.append(input('Adicione elementos a lista A:'))
    
if pico(a):
    print('S')
else:
    print('N')
