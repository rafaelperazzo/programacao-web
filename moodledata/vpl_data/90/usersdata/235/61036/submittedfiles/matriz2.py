# -*- coding: utf-8 -*-
m=int(input('digite o numero de colunas e linhas:'))
import numpy as np
a=np.zeros((m,m))
for i in range(0,a.shape[0],1):
        for j in range(0,a.shape[1],1):
            a[i,j]=float(input('digite um valor:'))


def listasoma(a):
    listadassomas=[]
    for i in range(0,a.shape[0],1):
        soma=0
        for j in range(0,a.shape[1],1):
            soma=soma+a[i,j]
        listadassomas.append(soma)
    for j in range(0,a.shape[1],1):
        soma=0
        for i in range(0,a.shape[0],1):
            soma=soma+a[i,j]
        listadassomas.append(soma)
    soma=0
    for i in range(0,a.shape[0],1):
        for j in range(0,a.shape[1],1):
            if i==j:
                soma=soma+a[i,j]
    listadassomas.append(soma)
    soma=0
    for i in range(a.shape[0]-1,-1,-1):
        for j in range(a.shape[1]-1,-1,-1):
            while a.shape[0]>-1:
                soma=soma+(a.shape[0]-1,a.shape[1]-1)
    listadassomas.append(soma)
    for i in range(0,len(listadassimas),1):
        if lista[i]==lista[i+1]:
            return S
        else:
            return N

a=magico
print(a)
        

