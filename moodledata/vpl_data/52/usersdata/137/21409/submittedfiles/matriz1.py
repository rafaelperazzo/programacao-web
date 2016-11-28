# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

def colunaEsquerda(a):
    for j in range (0,a.shape[1],1):
        for i in range(0,a.shape[0],1):
            if a[i,j]==1:
                return j
def colunaDireita(a):
    i=0
    j=a.shape[1]-1
    while j>=0:
        i=0
        while i<=a.shape[0]-1:
            if a[i,j]==1:
                return j
            i=i+i
        j=j-1
def linhaCima(a):
    for i in range (0,a.shape[0],1):
        for j in range (0,a.shape[1],1):
            if a[i,j]==1:
                return i
def linhaBaixo(a):
    i=a.shape[0]-1
    j=a.shape[1]-1
    while i>=0:
        j=a.shape[i]-1
        while j>=0:
            if(a[i,j])==1:
                return i
            j=j-1
        i=i-1

linhas =input('linhas:')
colunas=input('colunas:')
a=np.zeros((linhas,colunas))
for i in range (0,a.shape[0],1):
    for j in range (0,a.shape[1],1):
        a[i,j]=int(input('Digite um elemento:'))
ce=colunaEsquerda(a)
cd=colunaDireita(a)
lc=linhaCima(a)
lb=linhaBaixo(a)
print (a[lc:lb+1,ce:cd+1])
