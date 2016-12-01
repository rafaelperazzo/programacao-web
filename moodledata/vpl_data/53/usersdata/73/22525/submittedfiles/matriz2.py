# -*- coding: utf-8 -*-
from __future__ import division
def somaDiagonal1 (a):
    soma=0
    for i in range (0,a.shape[0],1):
        soma=soma+a[i,i]
    return soma
    
def somaDiagonal2 (a):
    soma=0
    i=0
    j=a.shape[0]-1
    while i<a.shape[0]:
        soma=soma+a[i,j]
        i=i+1
        j=j-1
    return soma
    
def somaLinhas (a):
    S=[]
    for i in range (0,a.shape[0],1):
        soma=0
        for j in range (0,a.shape[1],1):
            soma=soma+a[i,j]
        S.append(soma)
    return S
    
def somaColunas (a):
    S=[]
    for j in range (0,a.shape[1],1):
        soma=0
        for i in range(0,a.shape[0],1):
            soma=soma+a[i,j]
        S.append(soma)
    return S
    
def quadradoMagico (a):
    sd1=somaDiagonal1 (a)
    sd2=somaDiagonal2 (a)
    somaL=somaLinhas (a)
    somaC=somaColunas (a)
    cont=0
    for i in range (0,len(soma),1):
        if sd1==sd2==somaL[i]==somaC[i]:
            cont=cont+1
    if cont==len(soma):
        return True
    else:
        return False

n=input('digite n:')
a=np.zeros ((n,n))
for i in range (0,n,1):
    for j in range (0,n,1):
        a[i,j]=input('um valor:')

if quadradoMagico (a):
    print ('S')
else:
    print ('N')
