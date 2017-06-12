# -*- coding: utf-8 -*-
from __future__ import division
def lecker(lista):
    cont=0
    for i in range(0,len(lista),1):
        if i==0:
            if lista[i]>lista[i+1]:
            cont=cont+1
        elif i==len(lista)-1:
            if lista(i)>lista(i-1):
                cont=cont+1
            else:
                if lista[i]>lista[i-1]:
                    cont=cont+1
    if cont==1:
        return True
    else:
        return False
a=[]
b=[]
n=int(input('Quantidade de elementos: '))
for i in range(1,n+1,1):
    valor=float(input('1ªLista/ %dºNúmero: '))
    a.append(valor)
for i in range(1,n+1,1):
    valor=float(input(2ªLista/ %dºNúmero: '))
    b.append(valor)
if lista==lecker:
    print('S')
else:
    print ('N')