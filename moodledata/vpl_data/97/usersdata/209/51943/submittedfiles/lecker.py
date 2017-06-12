# -*- coding: utf-8 -*-
from __future__ import division
Def lecker(lista):
    cont=0
    for i in range (0,len(lista),1):
        if i==0:
            if lista[i]>lista[i+1]:
                cont=cont+1
        elif i==len(lista):
            if lista[i]<lista[i-1]:
                cont=cont+1
        else:
            if lista[i]>lista[i-1] and lista[i]>lista[i+1]:
                cont=cont+1
    if cont==1:
        return True
    else:
        return False
lista1=[]
n=int(input('Digite o tamnho da lista:'))
for i in range (1,n+1,1):
    x=float(input('Digite o elemento:'))
    lista.append(x)
    
    
        
        
