# -*- coding: utf-8 -*-
from __future__ import division
def lecker(lista):
    cont=0
    for i in range (0,len(lista),1):
        if i==0:
            if lista[i]>lista[i+1]:
                cont=cont+1
        if i==(len(lista)-1):
            if lista[i]>lista[i-1]:
                cont=cont+1
        else: 
            if lista[i]>lista[i-1] and lista[i].lista[i+1]:
                cont=cont+1
    if cont==1:
        return True
    else:
        return False
n=int(input('Digite o número de elementos da lista:'))
a=[]
for i in range (0,n,1):
     valor=int(input('Digite o valor a ser anexado à lista:'))
     a.append(valor)
    b=[]
for i in range (0,n,1):
    valor=int(input('Digite o valor a ser anexado à lista:'))
    b.append(valor)
if lecker(a)==True:
    print('S')
else:
    print('N')
if lecker(b)==True:
    print('S')
else:
    print('N')
    