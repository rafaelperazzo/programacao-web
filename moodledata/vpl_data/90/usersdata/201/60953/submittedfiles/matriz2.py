# -*- coding: utf-8 -*-
import numpy as np
def somaLinhas(b):
    soma=0
    for i in range(0,b.shape[0],1):
        for j in range(0,b.shape[1],1):
            soma=soma+b[i,j]
        return(soma)
        
def somaColunas(b):
    soma=0
    for j in range(0,b.shape[1],1):
        for i in range(0,b.shape[0],1):
            soma=soma+b[i,j]
        return(soma)
        
def somaDiagonalP(b):
    soma=0
    for i in range(0,b.shape[0],1):
        for j in range(0,b.shape[1],1):
            if i==j:
                soma=soma+b[i,j]
    return(soma)
    
def somaDiagonalS(b):
    soma=0
    i=0
    j=(b.shape[1])-1
    while i<b.shape[0]:
        soma=soma+b[i,j]
        i=i+1
        j=j-1
    return(soma)

n=int(input('Digite as linhas e as colunas:'))
b=np.zeros((n,n))

for i in range(0,b.shape[0],1):
    for j in range(0,b.shape[1],1):
        b[i,j]=float(input('Valor:'))
        
x=somaLinhas(b)
y=somaColunas(b)
w=somaDiagonaP(b)
z=somaDiagonalS(b)

if x==y and y==w and w==z:
    print('S')
else:
    print('N')






