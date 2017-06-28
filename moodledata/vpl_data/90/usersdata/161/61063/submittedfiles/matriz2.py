# -*- coding: utf-8 -*-
import numpy as np
n=int(input('Digite o número de linhas e colunas:'))
a=np.zeros((n,n))

for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=int(input('Digite um elemento:'))


def somalinha(a):
    soma=0
    for i in range(0,a.shape[0],1):
        for j in range(0,a.shape[1],1):
            soma=soma+a[i,j]
        return(soma)
        
def somacoluna(a):
    soma=0
    for j in range(0,a.shape[1],1):
        for i in range(0,a.shape[0],1):
            soma=soma+a[i,j]
        return(soma)
            
def somadiagonalPrincipal(a):
    soma=0
    for i in range(0,a.shape[0],1):
        for j in range(0,a.shape[1],1):
            if i==j:
                soma=soma+a[i,j]
    return(soma)    

def somadiagonalSecundaria(a):
    soma=0 
    i=0
    j=(a.shape[1])-1
    while i<a.shape[0]:
        soma=soma+a[i,j]
        i=i+1
        j=j-1
    return(soma)

x=somalinha(a)
y=somacoluna(a)
z=somadiagonalPrincipal(a)
w=somadiagonalSecundaria(a)

if x==y and y==z and z==w:
    print('S')
else:    
    print('N')
