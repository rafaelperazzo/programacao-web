# -*- coding: utf-8 -*-
import numpy as np
def somaLinha(a,x,T):
    soma=0
    for i in range (x,x+1,1):
        for j in range (0,a.shape[1],1):
            soma=soma+a[i,j]
    SomaF1=soma-T
    return(SomaF1)
    
def somaColuna(a,y,T):
    soma=0
    for j in range (y,y+1,1):
        for i in range (0,a.shape[0],1):
            soma=soma+a[i,j]
    SomaF2=soma-T
    return(SomaF2)
    
n=int(input('Digite o número de linhas e colunas: '))
x=int(input('Digite a primeira coordenada da posição da torre: '))
y=int(input('Digite a segunda coordenada da posição da torre: '))

a=np.zeros((n,n))
for i in range(0,a.shape[0],1):
    for j in range (0,a.shape[1],1):
        a[i,j]=int(input('Digite os termos da matriz: '))
        
T=a[x,y]
        
SomaTotal=(somaLinha(a,x,T))+(somaColuna(a,y,T))
print('%d' %SomaTotal)
        

