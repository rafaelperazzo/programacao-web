# -*- coding: utf-8 -*-
from __future__ import division
 def diagonalP(a):
     soma=0
     for i in range(0,a.shape[0],1):
        soma=soma+a[i,j]
        return soma
def diagonalS(a):
    soam=0
    i=0
    j=a.shape[0]-1
    while i<(a.shape[0]):
        soma=soma+a[i,j]
        i=i+1
        j=j-1
    return soma
def somalinhas(a):
    x=[]
    for i in range(0,a.shape[0],1):
        soma=0
        for j in range(0,a.shape[1],1):
            soma=soma+a[i,j]
        x.append(soma)
    return x
    
    
def somacolunas(a):
    x=[]
    for j in range(0,a.shape[1],1):
        soma=0
        for i in range(0,a.shape[0],1):
            soma=soma+a[i,j]
        x.append(soma)
    return x
    
def quadradomagico(a):
    dp=diagonalP(a)
    ds=diagonalS(a)
    sl=somalinhas(a)
    sc=somacolunas(a)
    
    contador=0
    for i in range(0,len(sl),1):
        if dp==ds==sl[i]==sc[i]:
            contador=contador+1
    
    if contador==len(sl):
        return True
    else:
        return False
        
d=input('digite o tamanho da matriz qaadrada:')

matriz=np.zeros((d,d))
for i in range(0,matriz.shape[0],1):
    for j in range(0,matriz.shape[1],1):
        matriz=[i,j]=input('digite o elemento da matriz:')

if quadradomagico(matriz):
    print('S')
else:
    print('N')