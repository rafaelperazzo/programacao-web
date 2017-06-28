# -*- coding: utf-8 -*-
import numpy as np
n=int(input('Informe a dimensão da matriz:'))
x=int(input('Informe a posição da linha:')) 
y=int(input('Informe a posição da coluna:'))
a=np.zeros((n,n))
    
for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=int(input('Informe um elemento da matriz:'))

def linha(a,i):
    soma=0
    for i in range(0,a.shape[0],1):
        soma=soma+a[i,j]
    return (soma)

def coluna(a,j):
    soma1=0
    for i in range(0,a.shape[1],1):
        soma1=soma1+a[j,i]
    return (soma1)    

b=linha(x,a)+coluna(y,a)-(2*a[x,y])      
print(b)

