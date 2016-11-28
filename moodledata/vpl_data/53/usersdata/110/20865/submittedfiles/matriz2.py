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
    j=a.shape[a]-1
    for i in range(0,a.shape[0],1):
        soma=soma+a[i,j]
        j=j-1
    return soma
def somaLinha(a):
    listasomaL=[]
    for i in range(0,a.shape[0],1):
        soma=0
        for j in range(0,a.shape,1):
            soma=soma+a[i,j]
            listasomaL.append(soma)
    return listasomaL
def somaColuna(a):
    listasomaC=[]
    for j in range(0,a.shape[0],1):
        soma=0
        for i in range(0,a.shape,1):
            soma=soma+a[i,j]
            listasomaC.append(soma)
    return listasomaC

def magico(a):
    listaTotal=[somap(a),somaS(a),somaLinha(a),somaColuna(a)]
    cont=0
    for i in range(0,len(listaTotal),1):
        if listaTotal[i]!=listaTotal[i+1]:
            cont=cont+1
    if cont==0:
        return True
    else:
        return False
linhas=input('Digite quant. linhas: ')
colunas=input('Digite quant. colunas: ')
a=np.zeros((linhas,colunas))
for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=input('Digite um valor: ')
if magico(a):
    print('Sim')
else:
    print('Não')
    
            