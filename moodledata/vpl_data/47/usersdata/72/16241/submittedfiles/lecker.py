# -*- coding: utf-8 -*-
from __future__ import division
#ENTRADA
def lecker(lista):
    cont=0
    for i in range(0,len(lista),1):
        if i==0:
            if x[i]>x[i+1]:
                cont=cont+1
        elif i==(len(x)-1):
            if x[i]>x[i-1]:
                cont=cont+1
        else:
            if (x[i]>x[i-1]) and (x[i]>x[i+1]):
                cont=cont+1
#PROCESAMENTO
a=[]
b=[]
n=input('digite a quantidade de elementos:')
for i in range(0,n,1):
    a.append(input('digite um elemento:'))
for i in range(0,n,1):
    b.append(input('digite um elemento:'))
                

