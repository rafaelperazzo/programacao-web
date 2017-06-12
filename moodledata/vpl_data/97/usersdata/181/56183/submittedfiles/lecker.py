# -*- coding: utf-8 -*-
from __future__ import division
def lecker(lista):
    cont=0
    for i in range(0,len(lista),1):
        if i==0:
            if lista[i]>lista[i+1]:
                cont=cont+1
        elif i==len(lista)-1:
            if lista[i]>lista[i-1]:
                cont=cont+1
        else:
            if lista[i]>lista[i+1] and lista[i]>lista[i-1]:
                cont=cont+1
    if cont==1:
        return True
    else:
        return False

n= int(input('n:'))
a=[]
b=[]
numero=float(input('numero:'))
for i in range (1,n+1,1):
    a.append(numero)
for i in range (1,n+1,1):   
    b.append(numero)
if lecker(a):
    print ('S')
else:
    print ('N')
if lecker(b):
    print ('S')
else:
    print ('N')