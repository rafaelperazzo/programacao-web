# -*- coding: utf-8 -*-
from __future__ import division

def lecker(lista):
    contador=0
    for i in range(0,n,1):
        if i==0:
            if lista[i]>lista[i-1]:
            contador=contador+1
            
        elif i==len(lista)-1:
            if lista[len(lista)-1]>lista[len(lista)-2]:
                contador=contador+1
        
    if contador==1:
        return true
    else:
        return false
        
n=input('digite o valor da lista:')
e=[]
d=[]

for i in range (0,n,1):
    e.append(input('digite valores:'))
    
for i in range (0,n,1):
    d.append(input('digite valores:'))

if lecker(lista):
    print ('S')
else:
    print ('N')
