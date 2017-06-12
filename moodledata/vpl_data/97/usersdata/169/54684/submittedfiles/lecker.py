# -*- coding: utf-8 -*-
from __future__ import division
n=int(input('Digite a Quantidade de Elementos:'))
l1=[]
l2=[]
for i in range(0,n,1):
    n1=int(input('Digite o Elemento da Lista:'))
    l1.append(n1)
for i in range(0,n,1):
    n2=int(input('Digite o Elemento da Lista:'))
    l2.append(n2)
def lecker(lista):
    cont=0
    if lista[0]>lista[1]:
     cont=cont+1
    elif lista[len(lista)-1] > lista[len(lista)-2]:
        cont=cont+1
    for i in range(1,len(lista)-1,1):
        if lista[i] > lista[i-1] and lista[i] > lista[i+1]:
            cont=cont+1
    if cont==1:
        return True
    if cont!=1: 
        return False
if lecker(l1):
    print('S')
else: 
    print('N')
if lecker(l2):
    print('S')
else:
    print('N')
