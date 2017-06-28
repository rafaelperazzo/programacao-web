# -*- coding: utf-8 -*-
import numpy as np
n=int(input('Informe o número de linhass e colunas:'))
a=np.zeros((n,n))

for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=int(input('Informe os elementos:'))

def soma_linha(a):
    lista=[]
    for i in range(0,a.shape[0],1):
        soma=0
        for j in range(0,a.shape[1],1):
            if i!=j:
                soma=soma+a[i,j]
        lista.append(soma)
    return(lista)
    
def diagonal_dominante(a,lista):
    for i in range(0,a.shape[0],1):
        for j in range(0,a.shape[1],1):
            if i==j:
                if a[i,j]>lista[i]:
                    return (True)
    return (False)
    
b=soma_linha(a)
if diagonal_dominante(a,b):
    print('SIM')
else:
    print('NÃO')
    
                

        