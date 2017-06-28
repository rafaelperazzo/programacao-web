# -*- coding: utf-8 -*-
import numpy as np

def soma(a):
    b=[]
    for i in range (0,a.shape[0],1):
        soma=0
        for j in range (0,a.shape[1],1):
            if i!=j:
                soma=soma+a[i,j]
                b.append(soma)
    return (b)

n=int(input('Tamanho da matriz:'))
a=np.zeros((n,n))
for i in range (0,a.shape[0],1):
    for j in range (0,a.shape[1],1):
        a[i,j]=int(input('Valor:'))
        
print(soma(a))
