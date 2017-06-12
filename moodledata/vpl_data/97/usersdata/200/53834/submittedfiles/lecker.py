# -*- coding: utf-8 -*-
from __future__ import division
def lecker (lista):
    cont=0
    for i in range (0,lend(lista),1):
        if i==0:
            if lista[i]>lista[i+1]:
                cont=cont+1
        elif i==(lend(lista)-1):
            if lista[i]>lista[i-1]:
                cont=cont+1
        else:
            if lista[i]>lista[i-1]:
                if lista[i]>lista[i+1]:
                    cont=cont+1
    if cont==1
        return True 
    else:
        return False 
        
n=int(input('coloque a quantidade de elementes da lista:'))

a=[]
for i in range (0,n,1):
    valor=int(input('Coloque o valor:'))
    a.append(valor)
    
b=[]
for i in range (0,n,1):
    valor=int(input('Coloque o valor:'))
    b.append(valor)
    
if lecker(a):
    print('S')
else:
    print('N')
    
if lecker(b):
    print('S')
else:
    print('N')