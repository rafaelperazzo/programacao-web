# -*- coding: utf-8 -*-
from __future__ import division

def arg(a):
    posicao=0:
    for i in range(0, len(a)-1,1):
        if a[i]>a[i+1]:
            posicao=i
                
    contador=0
    for i in range (posicao, len (a)-1,1):
        if a[i]<a[i+1]:
            contador=contador+1
    if contador==0 and posicao!=0:
        return true
    else:
        return false
        
#Entrada

a=[]
b=int(input('digite o valor de b:'))

#processamento

#decrescente

if decrescente (a):
    print ('S')
else:
    print ('N')
if decrescente (b):
    print ('S')
else:
    print ('N')
if decrescente (c):
    print ('S')
else:
    print ('N')

if consecutivos (a):
    print ('S')
else:
    print ('N')
if consecutivos (b):
    print ('S')
else:
    print ('N')
if consecutivos (c):
    print ('S')
else: 
    print ('N')



