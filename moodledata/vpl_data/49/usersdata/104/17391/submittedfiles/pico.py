# -*- coding: utf-8 -*-
from __future__ import division
def teste(lista):
    cont=0
    for i in range(0,len(lista),1):
        if i==len(lista):
            if cont==1:
                return True
                break
            else:
                return False
                break
        elif l[i]<l[i+1]:
            if cont==0:
                cont=0
            else:
                return False
                break
        else:
            cont=1
def pico(lista):
    if teste(lista):
        return ('S')
    else:
        return ('N')
        
n=input('Digite n digitos da lista:')
l=[]
for i in range(0,n,1):
    l.append(input('Digite um valor pra lista:'))
print pico(l)