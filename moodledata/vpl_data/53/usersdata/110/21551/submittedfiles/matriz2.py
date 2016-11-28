# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

def somap(a):
    soma=0
    for i in range(0,a.shape[0],1):
        soma=soma+a[i,i]
    return soma
def somaS(a):
    soma=0
    i=0
    j=a.shape[0]-1
    while i<a.shape[0]:
        soma=soma+a[i,j]
        j=j-1
        i=i+1
    return soma
def somaLinha(a):
    listasomaL=[]
    for i in range(0,a.shape[0],1):
        soma=0
        for j in range(0,a.shape[0],1):
            soma=soma+a[i,j]
        listasomaL.append(soma)
    return listasomaL
def somaColuna(a):
    listasomaC=[]
    for j in range(0,a.shape[0],1):
        soma=0
        for i in range(0,a.shape[1],1):
            soma=soma+a[i,j]
        listasomaC.append(soma)
    return listasomaC

def magico(a):
    cont=0
    prin=somap(a)
    sec=somaS(a)
    lista=somaLinha(a)
    lista2=somaColuna(a)
    for i in range(0,a.shape[0],1):
        if prin==sec==lista[i]==lista2[i]:
            cont=cont+1
    if  cont==len(lista):
        return True
    else:
        return False
            
    
linhas=input('Digite quant. linhas: ')
a=np.zeros((linhas,linhas))
for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=input('Digite um valor: ')
if magico(a):
    print('S')
else:
    print('N')
    
            