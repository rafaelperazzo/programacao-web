# -*- coding: utf-8 -*-
from __future__ import division

def crescente (lista):
    #escreva o código da função crescente aqui
    cont=0
    for i in range(0,len(lista)-1,1):
        if lista[i]<lista[i+1]:
            cont=cont+1
    if cont==len(lista)-1:
        return True
    else:
        return False
    
#escreva as demais funções
def decrescente (lista):
    cont=0
    for i in range(0,len(lista)-1,1):
        if lista[i]>lista[i+1]:
            cont=cont+1
    if cont==len(lista)-1:
        return True
    else:
        return False

def iguais (lista):
    cont=0
    for i in range(0,len(lista)-1,1):
        if lista[i]==lista[i+1]:
            cont=cont+1
    if cont>0:
        return True
    else:
        return False

#escreva o programa principal
