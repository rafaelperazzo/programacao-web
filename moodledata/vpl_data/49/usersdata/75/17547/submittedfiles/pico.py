# -*- coding: utf-8 -*-
from __future__ import division

def pico(lista):
    cont1=0
    for i in range (0,len(lista)-1,1):
        if lista[i]<lista[i+1]:
            cont1=cont1+1
    
    if cont1>0:
        return True
    else:
        return False
        
    for i in range (0,len(lista)-1,1):
        cont2=0
        if lista[i]>lista[i+1]:
            cont2=cont2+1
    
    if cont2>0:
        reurn True
    else:
        return False
        
    if cont1>0 and cont2>0:
        return True
    else:
        return False
    

n = input('Digite a quantidade de elementos da lista:')

a=[]

for i in range (0,n,1):
    a.append(input('Digite os termos da lista:'))
    
if pico(a):
    print ('S')
else:
    print ('N')
