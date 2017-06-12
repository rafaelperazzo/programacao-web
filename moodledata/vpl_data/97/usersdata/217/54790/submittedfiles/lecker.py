# -*- coding: utf-8 -*-
from __future__ import division
def lecker(lista):
    cont=0
    for i in range(0,len(lista)-1,1):
        if i==0:
            if lista[i]>lista[i+1]:
                cont=cont+1
        elif i==(len(lista)-1):
            if lista[i]>lista[i-1]:
                cont=cont+1
            else:
                if lista[i]>lista[i+1] andlista[i]>lista[i-1]:
                    cont=cont+1
    if cont==1:
        return True
    else:
        return False
a=[]
b=[]
n=int(input('digite n:'))
for i in range(i,n+1,1):
    valor=float(input('digite valor:'))
    a.append(valor)
for i in range(i,n+1,1):
    valor=float(input('digite valor:'))
    b.append(valor)
if lecker(a):
    print('N')
else:
    print('S')
if lecker(b):
    print('N')
else:
    print('S')
    
    
