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
    if somalinha(a)==somacoluna(a) and somalinha(a)==somadiagonal1(a) and somalinha(a)==somadiagonal2(a):
        if somacoluna(a)==somadiagonal1(a) and somacoluna(a)==somadiagonal2(a):
            if somadiagonal2(a)==somadiagonal1(a):
                return ('S')
    else:
        return ('N')
                    
print(quadrado_magico(a))                    