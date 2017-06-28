# -*- coding: utf-8 -*-
import numpy as np

def soma(a):
    soma=0
    b=[]
    for i in range(0,a.shape[0],1):
        for j in range(0,a.shape[1],1):
            soma=soma+a[i,j]
        b.append(soma)
    for j in range(0,a.shape[1],1):
        for i in range(0,a.shape[0],1):
            soma=soma+a[i,j]
        b.append(soma)
    for i in range(0,a.shape[0],1):
        for j in range(0,a.shape[1],1):
            if j==i:
                soma=soma+a[i,j]
    b.append(soma)   
    for i in range(0,a.shape[0],1):
        for j in range(0,a.shape[1],1):
            if i+j==a.shape[0]
                soma=soma+a[i,j]
    b.append(soma)
    return b

n=int(input('Tamanho da matriz:'))
a=np.zeros((n,n))
for i in range(0,a.shape[0],1):
        for j in range(0,a.shape[1],1):
            a[i,j]=float(input('Valor:'))
lista=soma(a)
cont=0
for i in range(0,len(lista)-1,1):
    if lista[i]==lista[i+1]:
        cont=cont+1
if cont==len(lista)-1:
    
