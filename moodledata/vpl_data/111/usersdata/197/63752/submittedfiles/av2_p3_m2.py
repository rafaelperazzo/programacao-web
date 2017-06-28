# -*- coding: utf-8 -*-
import numpy as np
n=int(input('Digite o numero de linhas e colunas:'))
a=np.zeros((n,n))
for i in range (0,a.shape[0],1):
    for j in range (0,a.shape[1],1):
        a[i,j]=int(input('Digite o valor de um numero da matriz:'))

def somalinha(b):
    soma=0
    lista=[]
    for i in range (0,b.shape[0],1):
        soma=0
        for j in range (0,b.shape[1],1):
            soma=soma+b[i,j]
        lista.append(soma)
    return (lista)
SOMAlinha=somalinha(a)
def somacoluna(b):
    soma=0
    lista=[]
    for j in range (0,b.shape[1],1):
        soma=0
        for i in range (0,b.shape[0],1):
            soma=soma+b[i,j]
        lista.append(soma)
    return (lista)
SOMAcoluna=somacoluna(a)

def diferente (lista):
    for i in range (0,len(lista),1):
        cont=0
        for j in range (0,len(lista),1):
            if i!=j:
                cont=cont+1
                
        if cont>1:
            return(i)
l=diferente(SOMAlinha)
c=diferente(SOMAcoluna)
print(a[l,c])
print(l)
print(c)
print(SOMAlinha)
print(SOMAcoluna)
