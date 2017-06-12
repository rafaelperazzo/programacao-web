# -*- coding: utf-8 -*-
from __future__ import division
def lecker()
    cont=0
    for i in range(0,len(lista),1):
        if i==0:
            if lista[i]>lista[i+1]:
                cont=cont+1
        elif i==len(lista)-1
            if lista[i]>lista[i-1]
                cont=cont+1
        else:
            if lista[i]>lista[i+1] and lista[i]>lista[i-1]
                cont=cont+1
        if cont==1:
            return True
        else:
            return False
n=int(input('Tamanho da lista: '))
r=[]
for i in range(1,n+1,1):
    numero=float(input('Digite os números: ')
    r.append(numero)
if def lecker(r):
    print('S')
else:
    print('N'