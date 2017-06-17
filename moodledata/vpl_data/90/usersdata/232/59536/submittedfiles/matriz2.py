# -*- coding: utf-8 -*-
import numpy as np
def SomaLinhas(a):
    soma=0
    for i in range(0,a.shape[0],1):
        for j in range(0,a.shape[1],1):
            soma=soma+a[i,j]
        return(soma)

def SomaColunas(a):
    soma=0
    for j in range(0,a.shape[1],1):
        for i in range(0,a.shape[0],1):
            soma=soma+a[i,j]
        return(soma)

def SomaDP(a):
    soma=0
    for i in range(0,a.shape[0],1):
        for j in range(0,a.shape[1],1):
            if i==j:
                soma=soma+a[i,j]
    return(soma)

def SomaDS(a):
    soma=0
    j=0
    i=a.shape[0]-1
    while j<a.shape[1]:
        soma=soma+a[i,j]
        j=j+1
        i=i-1
    return(soma)
        
n=int(input('Digite o número de linhas e colunas da matriz: '))
a=np.zeros((n,n))
for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=float(input('Digite o valor: '))
b=SomaLinhas(a)
c=SomaColunas(a)
d=SomaDP(a)
e=SomaDS(a)

if b==c and c==d and d==e:
    print('S')
else:
    print('N')
    
