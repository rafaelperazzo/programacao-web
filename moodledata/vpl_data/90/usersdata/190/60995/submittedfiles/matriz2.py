# -*- coding: utf-8 -*-
def linhas(a):
    somaL=[]
    for i in range(0,a.shape[0],1):
        soma=0
        for j in range(0,a.shape[1],1):
            soma=soma+a[i,j]
        somaL.append(soma)
    for k in range(0,len(somaL),1):
        if somaL[0]!=somaL[i]:
            return(False)
        else:
            return(somaL[0])

def colunas(a):
    somaC=[]
    for j in range(0,a.shape[1],1):
        soma=0
        for i in range(0,a.shape[0],1):
            soma=soma+a[i,j]
        somaC.append(soma)
    for k in range(0,len(somaC),1):
        if somaC[0]!=somaC[i]:
            return(False)
        else:
            return(somaC[0])

def diagonalPrincipal(a):
    soma=0
    for i in range(0,a.shape[0],1):
        soma=soma+a[i,i]
    return(soma)

def diagonalSecundaria(a):
    soma=0
    for i in range(0,a.shape[0],1):
        soma=soma+a[a.shape[0]-i-1,1]
    return(soma)
    
import numpy as np
n=int(input('digite n:'))
a=np.zeros((n,n))
for i in range(0,a.shape[0],1):
        for j in range(0,a.shape[1],1):
            a[i,j]=int(input('digite o valor:'))
            
x=linhas(a)
y=colunas(a)
z=diagonalPrincipal(a)
w=diagonalSecundaria(a)
if x==False or y==False:
    print('N')
else:
    if x==y==z==w:
        print('S')
    else:
        print('N')



