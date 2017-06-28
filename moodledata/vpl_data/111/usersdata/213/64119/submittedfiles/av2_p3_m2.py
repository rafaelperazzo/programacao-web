# -*- coding: utf-8 -*-
def linhas(matriz):
    linhas=[]
    for i in range(0,matriz.shape[0],1):
        soma=0
        for j in range(0,matriz.shape[1],1):
            soma=soma+matriz[i,j]
        linhas.append(soma)
    return (linhas)

def colunas(matriz):
    colunas=[]
    for j in range(0,matriz.shape[1],1):
        soma=0
        for j in range(0,matriz.shape[0],1):
            soma=soma+matriz[i,j]
        colunas.append(soma)
    return (colunas)

def termo(b):
    for i in range(0,len(b),1):
        contador=0
        for j in range(0,len(b),1):
            if b[i]==b[j]:    
                contador=contador+1
        if contador==1:
            return(i)

def numero(lista,termo):
    for i in range(0,len(lista),1):
        if i!=termo:
            numero=lista[termo]-lista[i]
            return (numero)

import numpy as np
n=int(input('Informe a quantidade de linhas e colunas da matriz: '))
matriz=np.zeros((n,n))
for i in range(0,matriz.shape[0],1):
    for j in range(0,matriz.shape[1],1):
        matriz[i,j]=int(input('Informe os elementos da matriz: '))

linhas=linhas(matriz)
colunas=colunas(matriz)

l=termo(linhas)
c=termo(colunas)

substituto=matriz[l,c]
original=substituto-(numero(linhas,l))

print('%d'%original)
print('%d'%substituto)
