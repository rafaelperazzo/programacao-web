# -*- coding: utf-8 -*-
from __future__ import division
def lecker (lista):
    cont=0
    for i in range(0,len(lista),1):
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
n=int(input('digite n:'))
lista1=[]
for i in range(0,n,1):
    valor=int(input('digite o valor:'))
    lista1.append(valor)
lista2=[]
for i in range(0,n,1):
    valor=int(input('digite o valor:'))
    lista2.append(valor)
if lecker(lista1):
    print('S')
else:
    print('N')
if lecker(lista2):
    print('S')
else:
    print('N')

