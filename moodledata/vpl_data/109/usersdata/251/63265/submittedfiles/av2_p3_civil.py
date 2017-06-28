# -*- coding: utf-8 -*-
import numpy as np

def somaDaLinha(x,torre,a):
    soma=0
    for i in range(x,x+1,1):
        for j in range(0,a.shape[1],1):
            soma=soma+a[i,j]
    somaTotal=soma-torre        
    return(somaTotal)

def somaDaColuna(y,torre,a):
    soma=0
    for j in range(y,y+1,1):
        for i in range(0,a.shape[0],1):
            soma=soma+a[i,j]
    somaTotal=soma-torre        
    return(somaTotal)

n=int(input('Digite a ordem da matriz: '))
x=int(input('Digite a cordenada da linha: '))
y=int(input('Digite a cordenada da coluna: '))

a=np.zeros((n,n))
for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=int(input('Digite o valor da casa: '))
        
torre=a[x,y]

l=somaDaLinha(x,torre,a)
c=somaDaColuna(y,torre,a)
peso=l+c
print('%.d'%peso)