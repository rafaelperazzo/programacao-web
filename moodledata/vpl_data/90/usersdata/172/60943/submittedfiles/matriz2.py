# -*- coding: utf-8 -*-
import numpy as np
def somalinhas(a):
    soma=0
    for i in range(0,a.shape[0],1):
        for l in range(0,a.shape[1],1):
            soma=soma+a[i,l]
        return(soma)
def somacolunas(a):
    soma=0
    for l in range(0,a.shape[1],1):
        for i in range(0,a.shape[0],1):
            soma=soma+a[i,l]
        return(soma)
def somadiagonal1(a):
    soma=0
    for i in range(0,a.shape[0],1):
        for l in range(0,a.shape[1],1):
            if i==l:
                soma=soma+a[i,l]
        return(soma)
def somadiagonal2(a):
    soma=0
    i=0
    l=(a.shape[1])-1
    while i<a.shape[0]:
        soma=soma+a[i,l]
        i=i+1
        l=l-1
    return(soma)
n=int(input('linhas: ')) 
a=np.zeros((n,n))
for i in range(0,a.shape[0],1):
    for l in range(0,a.shape[1],1):
        a[i,l]=float(input('valor:'))
x=somalinhas(a)
y=somacolunas(a)
w=somadiagonal1(a)
z=somadiagonal2(a)
if x==y and y==w and w==z:
    print('S')
else:
    print('N')
                
                

