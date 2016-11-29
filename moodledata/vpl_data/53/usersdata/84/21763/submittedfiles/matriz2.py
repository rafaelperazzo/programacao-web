# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

def somaDiagonal1(a):
    soma=0
    for i in range(0,a.shape[0],1):
        soma=soma+a[i,i]
    return soma
    
def somaDiagonal2(a):
    soma=0
    i=0
    j=a.shape[0]-1
    while i<a.shape[0]:
        soma=soma+a[i,j]
        i=i+1
        j=j+1
    return soma
    
def somaLinha(a):
    s=[]
    for i in range(0,a.shape[0],1):
        soma=0
        for j in range (0,a.shape[1],1):
            soma=soma+a[i,j]
        s.append(soma)
    return s

def somaColuna(a):
    s=[]
    for j in range(0,a.shape[1],1):
        soma=0
        for i in range(0,a.shape[0],1):
            soma=soma+a[i,j]
        s.append(soma)
    return s
    
def matrizMagica(a):
    
    sd1=somaDiagonal1(a)
    sd2=somaDiagonal2(a)
    
    somal=somaLinha(a)
    somac=somaColuna(a)
    
    cont=0
    for i in range(0,len(somal),1):
        if sd1==sd2==somal[i]==somac[i]:
            cont=cont+1
   
    if cont==len(somal):
        return True
    else:
        return False 

n=input('digite a dimensão da matriz:')
a=np.zeros((n,n))

for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=input('digite os elementos:')

if matrizMagica(a):
    print ('S')
else:
    print ('N')

        