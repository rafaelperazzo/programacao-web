# -*- coding: utf-8 -*-
import numpy as np
def somatorio (a):
    b=[]
    for i in range (0,a.shape[0],1):
        cont=0
        for j in range (0,a.shape[1],1):
            cont=0
            for j in range (0,a.shape[1],1):
                if i!=j:
                    cont=cont+a[i´j]
        b.append(b)
    return (b)
    
def diagonal(a,b):
    for i in range (0,a.shape[0],1):
        for j in range (0.a.shape[1],1):
            if i==j:
                if a[i,j]<b[i]:
                    return False
    return True

n=int(input('Digite o tamanho da matriz:'))
a.npzeros((n,n))
for i in range (0,a.shape[0],1):
    for j in range (0,a.shape[1],1):
        a[i,j]=int(input('Digite o valor de um numero da matriz:'))
b=csomatorio(a)
if diagonal(a,b):
    print('SIM')
relse:
    print('NAO')
