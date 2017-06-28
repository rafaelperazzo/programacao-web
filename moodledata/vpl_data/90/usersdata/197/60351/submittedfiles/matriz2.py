# -*- coding: utf-8 -*-
import numpy as np
n=int(input('Digite o numero de linhas e colunas:'))
a=np.zeros((n,n))
for i in range (0, a.shape[0],1):
    for j in range (0,a.shape[1],1):
        a[i,j]=float(input('Digite o valor:'))
def listadassomas (a):
    soma=0
    lista=[]
    for i in range (0,a.shape[0],1):
        soma=0
        for j in range (0,a.shape[1],1):
            soma=soma+a[i,j]
        lista.append(soma)
    for j in range (0,a.shape[1],1):
        soma=0
        for i in range (0,a.shape[0],1):
            soma=soma+a[i,j]
        lista.append(soma)
    soma=0
    for i in range (0,a.shape[0],1):
        for j in range (0,a.shape[1],1):
            if i==j:
                soma=soma+a[i,j]
        lista.append(soma)
        
    return (lista)
print(listadassomas(a))
    
    
    

    

