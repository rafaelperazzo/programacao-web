# -*- coding: utf-8 -*-
from __future__ import division

def pico(lista):
    cont=1
    for i in range (1,len(lista),1):
        if lista[i]>lista[i-1]:
            cont=cont+1
    if cont>1:
        for i in range(1,len(lista),1):
            if lista[i]<lista[i-1]:
                cont=cont+1
    return cont
    

n = input('Digite a quantidade de elementos da lista: ')
a=[]
for i in range (0,n,1):
    a.append(input('insira um valor para a lista:'))
    
    
if pico(a)==len(a):
    print ('S')
else:
    print ('N') 
    