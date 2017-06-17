# -*- coding: utf-8 -*-
import numpy as np
def SomaLinhas(a):
    soma1=0
    for i in range(0,a.shape[0],1):
        for j in range(0,a.shape[1],1):
            soma1=soma1+a[i,j]
        return(soma1)

def SomaColunas(a):
    soma2=0
    for j in range(0,a.shape[1],1):
        for i in range(0,a.shape[0],1):
            soma2=soma2+a[i,j]
        return(soma2)

def SomaDP(a):
    soma3=0
    for i in range(0,a.shape[0],1):
        for i in range(0,a.shape[1],1):
            if i==j:
                soma3=soma3+a[i,j]
        return(soma3)

def SomaDS(a):
    soma4=0
    for i in range(1,a.shape[0]-1,1):
        for j in range(1,a.shape[1],1):
            soma4=soma4+a[0+i,a.shape[1]-j]
        return(soma4)
        
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
    
