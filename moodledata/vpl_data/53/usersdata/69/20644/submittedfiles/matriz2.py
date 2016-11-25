# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np
def diagonalP(x):
    soma=0
    for i in range (0,x.shape[0],1):
        soma=soma+x[i,i]
    return soma
def diagonalS(x):
    soma=0
    for i in range(0,x.shape[0],1):
        soma=soma+x[i,x.shape[0]-i-1]
    return soma
def Slinha(x):
    l=[]
    for i in range (0,x.shape[0],1):
        soma=0
        for j in range(0,x.shape[1],1):
            soma=soma+x[i,j]
        l.append(soma)
    return l
def Scoluna(x):
    l=[]
    for j in range (0,x.shape[1],1):
        soma=0
        for i in range(0,x.shape[0],1):
            soma=soma+x[i,j]
        l.append(soma)
    return l

#NÃO PRECISA PEDIR A QUANTIDADE DE LINHAS E COLUNAS, POIS A MATRIZ TEM QUE SER QUADRADA!! ERA ESSE O ERRO!
n = input('Digite a dimensão da matriz: ')
a=np.zeros((n,n))
for i in range (0,a.shape[0],1):
    for j in range (0,a.shape[1],1):
        a[i,j]=input('Digite um número:')
p=diagonalP(a)
s=diagonalS(a)
t=Scoluna(a)
r=Slinha(a)
if p==s:
    cont=0
    for i in range(0,len(t),1):
        if p==t[i]==r[i]:
            cont=cont+1
    if cont==len(t):
        print 'S'
    else:
        print 'N'
else:
    print 'N'