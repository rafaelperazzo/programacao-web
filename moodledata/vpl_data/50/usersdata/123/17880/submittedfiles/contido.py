# -*- coding: utf-8 -*-
from __future__ import division

def quant(lista1,lista2):
    i=0
    cont=0
    while i <len(lista1):
        j=0
        while j<len(lista2):
            if lista1[i]==lista2[j]:
                cont=cont+1
            j=j+1
        i=i+1
    return cont
n= input('Insira a quantidade de valores de a:')
m= input('Insira a quantidade de valores de b:')
a=[]
b=[]
for i in range (0,n,1):
    a.append(input('Insira um valor para a:'))
for i in range (0,m,1):
    b.append(input('Insira um valor para b:'))
elementos=quant(a,b)
print (elementos)