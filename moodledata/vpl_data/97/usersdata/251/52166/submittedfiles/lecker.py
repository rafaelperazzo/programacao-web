# -*- coding: utf-8 -*-
from __future__ import division
lista1=[]
lista2=[]
n = int(input('Digite a quantidade de termos da lista: '))
for i in range(0,n,1):
    termo = int(input('Digite o valor do termo '+str(i)+' da lista 1: '))
    lista1.append(termo)
    
for i in range(0,n,1):
    termo = int(input('Digite o valor do termo '+str(i)+' da lista 2: '))
    lista2.append(termo)

def lecker(lista):
    cont=0
    if lista[0]>lista[1]:
        cont=cont+1
    elif lista[len(lista)-1]>lista[len(lista)-2]:
        cont=cont+1
    for a in range(1,len(lista)-1,1):
        if lista[a]>lista[a-1] and lista[a]>lista[a+1]:
            cont=cont+1
        else:cont=cont    
    if cont==1:
        return('S')
    else:
        return('N')
        
print(lecker(lista1))
print(lecker(lista2))