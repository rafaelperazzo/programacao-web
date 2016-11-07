# -*- coding: utf-8 -*-
from __future__ import division
def comparar(lista):
    cont=0
    for i in range (0,len(lista),1):
        if i==0:
            if lista[i]>lista[i+1]:
                cont=cont+1
            
        elif i==len(lista)-1:
            if lista[i]>list[i-1]:
                cont=cont+1
                
        else:
            if lista[i]>lista[i+1] and lista[i]>lista[i-1]:
                cont=cont+1
    if cont==1:
        return True
    else:
        return False
a=[]
b=[]
n=input('digite a quantidade de números:')
for i in range(0,n,1):
    a.append(input('digite um número:'))
for i in range(0,n,1):
    b.append(input('digite um número:'))
if comparar(a):
    print('S')
else:
    print('N')
if comparar(b):
    print('S')
else:
    print('N')
    