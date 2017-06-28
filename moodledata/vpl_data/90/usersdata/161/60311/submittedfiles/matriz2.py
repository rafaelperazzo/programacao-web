# -*- coding: utf-8 -*-
import numpy as np
linhas=int(input('Informe o número de linhas:'))
colunas=int(input('Informe o número de colunas:'))
a=np.zeros((linhas,colunas))

for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=int(input('Digite um elemento:'))

def somalinha(a):
    lista=[]
    for i in range(0,a.shape[0],1):
        soma=0
        for j in range(0,a.shape[1],1):
            soma=soma+a[i,j]
        lista.append(soma)    
    return(lista)        

def somacoluna(a):
    lista1=[]
    for j in range(0,a.shape[1],1):
        soma=0
        for i in range(0,a.shape[0],1):
            soma=soma+a[i,j]
        lista1.append(soma)
    return(lista1)

def diagonal1(a):
    soma=0
    lista2=[]
    for i in range(0,a.shape[0],1):
        for j in range(0,a.shape[1],1):
            if i==j:
                soma=soma+a[i,j]
        lista2.append(soma)        
    return (lista2)
    
def diagonal2(a):
    soma=0
    lista3=[]
    for i in range(0,a.shape[0],1):
        for j in range(0,a.shape[1],1):
            if i+j==n+1:
                soma=soma+a[i,j]
        lista3.append(soma)
    return(lista3)    
                
def quadrado_magico(a):
    if somalinha==somacoluna and somalinha==somadiagonal1 and somalinha==somadiagonal2:
        if somacoluna==somadiagonal1 and somacoluna==somadiagonal2:
            if somadiagonal2==somadiagonal1:
                return True
                else:
                    return False
                    
print(quadrado_magico(a))                    