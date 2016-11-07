# -*- coding: utf-8 -*-
from __future__ import division

#função lecker

def lecker(lista):
    cont=0
    for i in range (0,len(lista),1):
        if i==0:
            if lista[i]>lista[i+1]:
                cont = cont+1
        elif i ==(len(lista)-1):
            if lista[i]>lista[i-1]:
                cont=cont+1
        else:
            if lista[i]>lista[i-1] and lista[i]>lista[i+1]:
                cont=cont+1
    if cont==1:
        return True
    else:
        return False

#programa principal

n=input('Digite um valor n:')

a=[]
b=[]

for i in range (0,n,1):
    a.append(input('Digite um valor:'))

for i in range (0,n,1):
    b.append(input('Digite um valor:'))