# -*- coding: utf-8 -*-
def linha (a):
    for i in range (0,a.shape[0],1):
        for j in range (0,a.shape[1],1):
            if a[i,j]==1:
                return i
def Linha(a):
    for i in range (a.shape[0]-1,-1,-1):
        for j in range (0,a.shape[1],1):
            if a[i,j]==1:
                return i
def coluna(a):
    for j in range (0,a.shape[1],1):
        for i in range (0,a.shape[0],1):
            if a[i,j]==1:
                return j
def Coluna(a):                
    for j in range (a.shape[1]-1,-1,-1):
        for i in range (0,a.shape[0],1):
            if a[i,j]==1:
                return j
n=int(input('digite a quantidade de linhas:'))
m=int(input('digite a quantidade de colunas:'))
import numpy as np
a=np.zeros( (n,m) )
for i in range (0,a.shape[0],1):
    for j in range (0,a.shape[1],1):
        a[i,j]=int(input('digite o elemento da matriz:'))
print(a[linha(a):(Linha(a)+1),coluna(a):(Coluna(a)+1)])
print(linha(a))
print(Linha(a))
print(coluna(a))
print(Coluna(a))