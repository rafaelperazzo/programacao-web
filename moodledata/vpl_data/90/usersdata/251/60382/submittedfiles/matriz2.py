# -*- coding: utf-8 -*-
import numpy as np

def somaLinhas(a):
    soma=0
    for i in range(0,a.shape[0],1):
        for j in range(0,a.shape[1],1):
            soma=soma+a[i,j]
    return(soma)

def somaColunas(a):
    soma=0
    for j in range(0,a.shape[1],1):
        for i in range(0,a.shape[0],1):
            soma=soma+a[i,j]
    return(soma)        

def somaDP(a):
    soma=0
    for i in range(0,a.shape[0],1):
        for j in range(0,a.shape[1],1):
            if i==j:
                soma=soma+a[i,j]
    return(soma)
    
def somaDS(a):
    soma=0
    i=0
    j=(a.shape[1])-1
    
    while i<a.shape[0]:
        soma=soma+a[i,j]
        i=i+1
        j=j-1
        
    return(soma)    
    
n = int(input('Digite o número de linhas e colunas da matriz quadrada :'))
a=np.zeros((n,n))

for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=float(input('Digite o valor do termo :'))
        
b=somaLinhas(a)
c=somaColunas(a)
d=somaDP(a)
e=somaDS(a)

if b==c and c==d and d==e:
    print('S')
else:
    print('N')