# -*- coding: utf-8 -*-
from __future__ import division

#COMECE AQUI ABAIXO
def crescente(lista):
    cont=0
    for i in range(0,(len(lista)-2),1):
        if lista[i]<lista[i+1]:
            cont=cont
        else:
            cont=cont+1
    if cont==0:
        return True
    else:
        return False

n=input('n:')
a=[]
for i in range(0,n,1):
    a.append(input('Digite um valor:'))

print crescente(a)