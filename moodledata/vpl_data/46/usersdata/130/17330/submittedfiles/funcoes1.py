# -*- coding: utf-8 -*-
from __future__ import division

def crescente (lista):
    cont=0
    for i in range(0,len(lista),1):
        if lista[i]>lista[i+1]:
            cont=cont+1
    if cont==len(lista)-1:
        return True
    else:
        return False
def decrescente (lista):
    cont=0
    i=len(lista)-1
    while i>=0:
        if lista[i]>lista[i-1]:
            cont=cont+1
        i=i-1    
    if cont==len(lista)-1:
        return True
    else:
        return False
    
def 

#escreva as demais funções





#escreva o programa principal
