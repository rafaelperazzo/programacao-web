# -*- coding: utf-8 -*-
import numpy as np

def menorColuna(a):
    for j in range (0,a.shape[1],1):
        for i in range (0,a.shape[0],1):
            if a[i,j]==1:
                return j
                
def maiorColuna(a):
    for j in range (0,a.shape[1],1):
        for i in range (0,a.shape[0],1):
            if a[i,j]==1:
                cd=j
    return cd
                
def menorLinha(a):
    for i in range (0,a.shape[0],1):
        for j in range (0,a.shape[1],1):
            if a[i,j]==1:
                return i
                
def maiorLinha(a):
    for i in range (0,a.shape[0],1):
        for j in range (0,a.shape[1],1):
            if a[i,j]==1:
                lb=i
    return lb
    
    
linhas=input('Digite o número de linhas da matriz:')
colunas=input('Digite o número de colunas da matriz:')

a=np.zeros((linhas,colunas))

for i in range (0,a.shape[0],1):
    for j in range (0,a.shape[1],1):
        a[i,j]=input('Digite um elemento da matriz:')
        
print menorColuna(a)

print maiorColuna(a)

print menorLinha(a)

print maiorLinha(a)

print (a[i:lb+1,j:cd+1])