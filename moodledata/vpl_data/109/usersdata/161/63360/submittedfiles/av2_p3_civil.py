# -*- coding: utf-8 -*-
import numpy as np
n=int(input('Informe a dimensão da matriz:'))
x=int(input('Informe a posição da linha:')) 
y=int(input('Informe a posição de coluna:))
a=np.zeros((n,n))
    
for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=int(input('Informe um elemento da matriz:'))

def linha(a,x):
    soma=0
    for i in range(0,a.shape[0],1):
        soma=soma+x[i,a]
    return (soma)

def coluna(a,y):
    soma1=0
    for i in range(0,a.shape[1],1):
        soma1=soma1+y[a,i]
    return (soma1)    
        
print(linha(x,a)+coluna(y,a)-(2*a[x,y]))

