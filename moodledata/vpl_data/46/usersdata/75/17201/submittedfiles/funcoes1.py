# -*- coding: utf-8 -*-
from __future__ import division

def crescente (lista):
    for i in range (0,len(lista),1):
        if lista[i]<lista[i+1]:
            return True
        else:
            return False
            
def decrescente (lista):
    for i in range (0,len(lista),1):
        if lista[i]>lista[i+1]:
            return True
        else:
            return False
            
def consecutivos(lista):
    for i in range (0,len(lista),1):
        if lista[i]==lista[i+1]:
            return True
        else:
            return False
            
n=int(input('Digite o número de termos das listas:'))
a=[]
b=[]
c=[]




#escreva as demais funções





#escreva o programa principal
