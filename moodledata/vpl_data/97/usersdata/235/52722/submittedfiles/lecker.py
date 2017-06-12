# -*- coding: utf-8 -*-
from __future__ import division
def lecker (lista):
    cont=0
    for i in range (0,len(lista),1):
        if i==0:
            if lista[i]>lista[i+1]:
                cont=cont+1
            elif i==len(lista)-1:
                if lista[i]>lista[i-1]:
                    cont=cont+1
            else:
                if lista[i]>lista[i-1]:
                    if lista[i]>lista[i+1]:
                        cont=cont+1
    if cont==1:
        return True
    else:
        return False
n=int(input('digite o n da lista:'))

a=[]
b=[]
for i in range (0,n,1):
    valor=int(input('digite um valor:'))
    a.append(valor)
for i in range (0,n,1):
    valor=int(input('digite um valor:'))
    b.append(valor)
    
if lecker(a):
    print('S')
else:
    print('N')
if lecker(b):
    print('S')
else:
    print ('N')