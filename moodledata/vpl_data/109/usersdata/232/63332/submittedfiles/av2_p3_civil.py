# -*- coding: utf-8 -*-
import numpy as np
def soma(a,x,y):
    soma=0
    torre=a[x,y]
    for i in range(0,a.shape[0],1):
        for j in range(0,a.shape[1],1):
            if a[i,j]==a[x,j]:
                soma=soma+a[i,j]
            elif a[i,j]==a[i,y]:
                soma=soma+a[i,j]
            else:
                soma=soma
    somaF=soma-torre
    
    return(somaF)

n=int(input('Digite o número de linhas e colunas: '))
x=int(input('Digite a primeira coordenada da posição da torre: '))
y=int(input('Digite a segunda coordenada da posição da torre: '))
a=np.zeros((n,n))
for i in range(0,a.shape[0],1):
    for j in range (0,a.shape[1],1):
        a[i,j]=int(input('Digite os termos da matriz: '))
        
print(soma(a,x,y))
        

