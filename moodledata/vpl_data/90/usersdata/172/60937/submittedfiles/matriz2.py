# -*- coding: utf-8 -*-
import numpy as np
def somalinhas(a):
    soma=0
    for i in range(0,a.shape[0],1):
        for j in range(0,a.shape[1],1):
            soma=soma+a[i,j]
        return(soma)
def somacolunas(a):
    soma=0
    for j in range(0,a.shape[1],1):
        for i in range(0,a.shape[0],1):
            soma=soma+a[i,j]
        return(soma)
def somadiagonal1(a):
    soma=0
    for i in range(0,a.shape[0],1):
        for j in range(0,a.shape[1],1):
            if i==j:
                soma=soma+a[i,j]
        return(soma)
def somadiagonal2(a):
    soma=0
    i=0
    j=(a.shape[1])-1
    while i<a.shape[0]:
        soma=soma+a[i,j]
        i=i+1
        j=j-1
    return(soma)
n=int(input('dimensão: ')) 
a=np.zeros((n,n))
for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=float(input('valor:'))
x=somalinhas(a)
y=somacolunas(a)
w=somadiagonal1(a)
z=somadiagonal2(a)
if x==y and y==w and w==z:
    print('S')
else:
    print('N')
                
                

