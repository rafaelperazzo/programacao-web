# -*- coding: utf-8 -*-
from __future__ import division

def leker(lista):
    cont=0
    for i in range(0,len(lista)-1,1):
        if i==0:
            if lista[i]>lista[i+1]:
                cont=cont+1
        elif i==(len(lista)-1):
            if lista[i]>lista[i-1]:
                cont=cont+1
            else:
                if lista[i]>lista[i+1] and lista[i]>lista[i-1]:
                    cont=cont+1
    if cont==1:
        return True
    else:
        return True 
a=[]
b=[]
n=int(input('quantidade:'))
for i in range(1,n+1,1):
    valor=float(input('lista')
    
for i in range(1,n+1,1):
    valor=float(input('lista')
   
if leker(a):
    print('N')
else:
    print('S')
if leker(B): 
    print('N')
else:
    print('S')
    