# -*- coding: utf-8 -*-
import numpy as np
def soma2(a):
    soma=0
    j=0
    i=a.shape[0]-1
    while j<a.shape[1]:
        soma=soma+a[i,j]
        j=j+1
        i=i-1
    return soma
def soma1(a):
    soma=0
    for i in range(a.shape[0]):
        for j in range (a.shape[1]):
            if i==j:
                soma=soma+a[i,j]
    return soma
def somai(a):
    soma=0
    for i in range(a.shape[0]):
        a=soma
        cont=0
        soma=0
        for j in range(a.shape[1]):
            soma=soma+a[i,j]
        if soma>a:
            cont=cont+1
    if cont>1:
        return (10101010101010101010101)
    else:
        return soma
def somaj(a):
    soma=0
    for j in range(a.shape[1]):
        a=soma
        cont=0
        soma=0
        for i in range(a.shape[0]):
            soma=soma+a[i,j]
        if soma>a:
            cont=cont+1
    if cont>1:
        return (10101010101010101010101)
    else:
        return soma
n=int(input('n:'))
MA=np.zeros((n,n))
for i in range(MA.shape[0]):
    for j in range(MA.shape[1]):
        MA[i,j]=float(input('numero:'))
cont=0
if soma2(MA)!=soma1(MA) or soma2(MA)!=somai(MA) or soma2(MA)!= somaj(MA):
    cont=cont+1
elif soma1(MA)!=somai(MA) or soma1(MA)!=somaj(MA):
    cont=cont+1
elif somaj(MA)!=somai(MA):
    cont=cont+1
if cont>0:
    print('N')
else:
    print('S')
    

