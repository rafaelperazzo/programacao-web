# -*- coding: utf-8 -*-
import numpy as np
n=int(input('Digite o numero de linhas e colunas:'))
a=np.zeros((n,n))
for i in range (0,a.shape[0],1):
    for j in range (0,a.shape[1],1):
        a[i,j]=float(input('Digite o valor de um numero da matriz:')
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
def sdp(b):
    i=0
    j=0
    soma=0
    while i<b.shape[1]:
        i=i+1
        j=j+1
        soma=soma+b[i,j]
    return(soma)
SDP=sdp(a)
def sds(b):
    i=0
    j=b.shape[0]-1
    soma=0
    while i<b.shape[1]:
        i=i+1
        j=j-1
        soma=soma+b[i,j]
    return(soma)
SDS=sds(a)
for i in range (0,a.shape[0],1)