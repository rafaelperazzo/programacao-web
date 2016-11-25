# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np
def colunaEsquerda(a):
    ce=0
    for j in range (0,a.shape[1],1):
        for i in range (0,a.shape[0],1):
            if a[i,j]==1:
                return j #<------------------- ERRO ESTAVA AQUI! CORRIGIDO!
                
    
def colunaDireita(a):
    cd=0
    i=0
    j=a.shape[1]-1
    while j>=0:
        while i<=a.shape[0]-1:
            if a[i,j]==1:
                return j #<------------------- ERRO ESTAVA AQUI! CORRIGIDO! não precisava do break
            i=i+1
        j=j-1
        
def linhaCima(a):
    lc=0
    for i in range (0,a.shape[0],1):
        for j in range (0,a.shape[1],1):
            if a[i,j]==1:
                return i #<------------------- ERRO ESTAVA AQUI! CORRIGIDO!
                

def linhaBaixo(a):
    lb=0
    i=a.shape[0]-1
    j=a.shape[1]-1
    while i<=a.shape[0]-1 and i>=0:
        while j<=a.shape[1]-1 and j>=0:
            if a[i,j]==1:
                return i #<------------------- ERRO ESTAVA AQUI! CORRIGIDO!
            j=j-1
        i=i-1

linhas=input('digite a quantidade de linhas:')
colunas=input('digite a quantidade de colunas:')
a=np.zeros((linhas,colunas))
for i in range (0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=input('digite um elemento:')
ce=colunaEsquerda(a)
cd=colunaDireita(a)
lc=linhaCima(a)
lb=linhaBaixo(a)
print a
print ce
print cd
print lc
print lb
#print (a[lc:lb+1,ce:cd+1])
    
    
    
    
    
    
    
    
    
    
    