# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

def sColunas(a):
    b=[]
    soma=0
    for j in range(0,a.shape[1],1):
        soma=0
        for i in range(0,a.shape[0],1):
            soma=soma + a[i,j]
        b.append(soma)
    return b
    
def sLinhas(a):
    b=[]
    soma=0
    for i in range(0,a.shape[0],1):
        soma=0
        for j in range(0,a.shape[1],1):
            soma=soma + a[i,j]
        b.append(soma)
    return b
    
def diagonalP(a):
    soma =0
    for i in range(0,a.shape[0],1):
        soma=soma+a[i,i]
    return soma

def diagonalS(a):
    soma=0
    j=a.shape[1]-1
    i=0
    while j>=0 and i<a.shape[0]:
        soma=soma+a[i,j]
        j=j-1
        i=i+1
    return soma
    
def perfeito(a):
    l=sColunas(a)
    f=sLinhas(a)
    d=diagonalP(a)
    c=diagonalS(a)
    cont=0
    for i in range (0,len(l)-1,1):
        if l[i]!=l[i+1]:
            cont= cont+1
    if cont!=0:
        return False
    else:
        cont2=0
        for i in range (0,len(f)-1,1):
            if f[i]!=f[i+1]:
                cont2= cont2+1
        if cont2!=0:
            return False
        else:
            if l[0]==f[0] and l[0]==d and l[0]==c:
                return True
            else:
                return False

n= input('Insira a dimensão:')
a=np.zeros((n,n))
for i in range (0,a.shape[0],1):
    for j in range (0,a.shape[1],1):
        a[i,j]= input('Insira um valor':)
if perfeito(a):
    print('S')
else:
    print('N')