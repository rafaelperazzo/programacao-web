# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np
linhas=input('Digite a quantidade de linhas:')
colunas=input('Digite a quantidade de colunas:')
a=np.zeros((linhas,colunas))
for i in range (0,a.shape[0],1):
    for j in range (0,a.shape[1],1):

def somadp(a):
    soma=0
    for i in range(0,a.shape[0],1):
        soma=soma+a[i,i]
    return soma
    
def somads(a):
    soma=0
    i=0
    j=a.shape[0]
    while i<a.shape[0]:
        soma=soma+a[i,j]
        i=i+1
        j=j-1
    return soma
    
def somaL(a):
    S=[]
    for i in range(0,a.shape[0],1):
        soma=0
        for j in range(0,a.shape[1],1):
            soma=soma+a[i,j]
        S.append(soma)
    return S

def somaLi(a):
    S=[]
    for i in range(0,a.shape[0],1):
        soma=0
        for j in range(0,a.shape[1],1):
            soma=soma+a[i,j]
        S.append(soma)
    return S
  
sd=somadp(a)
sd2=somads(a)
sl=somaLi(a)
sll=somaL(a)
cont=0
for i in range (0,len(somaL),1):
    if sll==sl==sd2[i]==sd[i]:
        cont=cont+1
if cont==len(somaL):
    return True
else:
    return False
    
if quadradomagico(a):
    print 'S'
else:
    print 'N'