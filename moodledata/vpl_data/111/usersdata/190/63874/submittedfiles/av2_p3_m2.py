# -*- coding: utf-8 -*-
import numpy as np
def somaLinhas(a):
    somaLinhas=[]
    for i in range(0,a.shape[0],1):
        soma=0
        for j in range(0,a.shape[0],1):
            soma=soma+a[i,j]
        somaLinhas.append(soma)
    return(somaLinhas)
    
def somaColunas:
    somaColunas=[]
    for j in range(0,a.shape[1],,1):
        soma=0
        for i in range(0,a.shape[0],1):
            soma=soma+a[i,j]
        somaColunas.append(soma)
    return(somaColunas)
    
def 
        

    
n=int(input('digite n:'))
a=np.zeros((n,n))
for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=int(input('digite o valor:'))


