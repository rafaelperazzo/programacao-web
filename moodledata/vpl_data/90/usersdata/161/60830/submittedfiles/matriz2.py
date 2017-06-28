# -*- coding: utf-8 -*-
import numpy as np
linhas=int(input('Informe o número de linhas:'))
colunas=int(input('Informe o número de colunas:'))
a=np.zeros((linhas,colunas))

for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=int(input('Digite um elemento:'))

def somalinha(a):
    for i in range(0,a.shape[0],1):
        soma=0
        for j in range(0,a.shape[1],1):
            soma=soma+a[i,j]
        return(soma)
        
def somacoluna(a):
    for j in range(0,a.shape[1],1):
        soma=0
        for i in range(0,a.shape[0],1):
            soma=soma+a[i,j]
            return(soma)
            
def somadiagonal1(a):
    soma=0
    for i in range(0,a.shape[0],1):
        for j in range(0,a.shape[1],1):
            if i==j:
                soma=soma+a[i,j]
        return(soma)    

def somadiagonal2(a):
    soma=0 
    i=0
    n=(a.shape[1])-1
    while i<a.shape[0]:
        soma=soma+a[i,j]
        i=i+1
        n=n-1
    return(soma)
    
x=somalinha(a)
y=somacoluna(a)
w=somadiagonal1(a)
z=somadiagonal2(a)

if x==y and y==w and w==z:
    print('S')
else:    
    print('N')
