# -*- coding: utf-8 -*-
from __future__ import division
lista=[]
n = int(input('Digite a quantidade de termos da lista: '))
for i in range(0,n,1):
    termo = int(input('Digite o valor do termo '+str(i)+': '))
    lista.append(termo)

cont=0
for i in range(0,len(lista),1):
    if lista[i]>lista[i-1] and lista[i]>lista[i-1]:
        cont=cont+1

if cont==1:
    print('S')
else:
    print('N')
