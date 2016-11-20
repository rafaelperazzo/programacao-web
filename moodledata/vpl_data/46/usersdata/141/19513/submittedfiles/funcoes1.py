# -*- coding: utf-8 -*-
from __future__ import division

def crescente (lista):
c=0
for i in range(0, len(lista) - 1, 1):
    if(lista[i]>lista[i+1]):
        c= c + 1
if c== 0:
    return True
else:
    return False
    
def decrescente (lista):
    c=0
    for i in range (0, len(lista)-1,1):
        if(lista[i]<lista[i+1]):
            c=c+1
    if c==0:
        return True
    else:
        return False

def iguais(lista):
    c=0
    for i in range(0, len[lista] - 1, 1):
        if(lista[i]==lista[i+1]):
            c=c+1
    if c!=0:
        return True
    else:
        return False
def insere lista(lista,n):
    for i in range(0,n,1):
        lista.append(input('digite o elemento:'))
    return lista
    




#escreva o programa principal
