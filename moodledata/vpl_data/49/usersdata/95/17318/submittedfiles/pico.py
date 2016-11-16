# -*- coding: utf-8 -*-
from __future__ import division

def pico(lista):
    i=0
    if lista[i]<lista[i+1]:
        cresce=True
        while i<len(lista) and lista[i]<lista[i+1]:
            i=i+1
    
    if lista[i]>lista[i+1]:
        decresce=True
        while i<len(lista) and lista[i]>lista[i+1]:
            i=i+1
        
    if lista[i]<lista[i+1]:
        cresce2=True
        while i<len(lista) and lista[i]<lista[i+1]:
            i=i+1

    if cresce and decresce:
        return True
    else:
        return False
        
n = input('Digite a quantidade de elementos da lista: ')
#CONTINUE...
a=[]
for i in range(0,n,1):
    a.append(input('a:'))

if pico(a)==True:
    print ('S')
else:
    print('N')