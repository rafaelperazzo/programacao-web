# -*- coding: utf-8 -*-
import numpy as np
n=int(input('Digite a dimensão da matriz:'))
a=np.zeros((n,n))

for i in range(0,a.shape[0],1):
    for j in ranf=ge(0,a.shape[1],1):
        a[i,j]=int(input('Informe um elemento da matriz:'))

def somalinha(a):
    soma=0
    for i in range(0,a.shape[0],1):
        for j in range(0,a.shape[1],1):
            soma=soma+a[i,j]
    return(soma)

def somacoluna(a):
    soma=0
    for i in range(0,a.shape[1],1):
        for j in range(0,a.shape[0],1):
            soma=soma+a[i,j]
    return(soma)    

    
    
        


