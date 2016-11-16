# -*- coding: utf-8 -*-
from __future__ import division

def pico(lista):
    i=cresce=decresce=cresce2=0
    if lista[i]<lista[i+1]:
        i+=1
        cresce=1
    while i<n and lista[i]<lista[i+1]:
        i=i+1
    
    if lista[i]>lista[i+1]:
        i=i+1
        decresce=1
    while i<n and lista[i]>lista[i+1]:
        i=i+1
        
    if lista[i]<lista[i+1]:
        cresce2=1
    while i<n and lista[i]<lista[i+1]:
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