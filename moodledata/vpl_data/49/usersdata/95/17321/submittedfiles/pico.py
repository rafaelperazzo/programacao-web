# -*- coding: utf-8 -*-
from __future__ import division

def pico(lista):
    i=c=d=c2=0
    if lista[i]<lista[i+1]:
        c=1
        while i<len(lista) and lista[i]<lista[i+1]:
            i=i+1
    
    if lista[i]>lista[i+1]:
        d=1
        while i<len(lista) and lista[i]>lista[i+1]:
            i=i+1
        
    if lista[i]<lista[i+1]:
        c2=1
        while i<len(lista) and lista[i]<lista[i+1]:
            i=i+1

    if cresce==1 and decresce==1:
        return True
    else:
        return False
        
n = input('Digite a quantidade de elementos da lista: ')
#CONTINUE...
a=[]
for i in range(0,n,1):
    a.append(input('a:'))

if pico(a):
    print ('S')
else:
    print('N')