# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np
def colunaesquerda(a):
    for j in range (0,a.shape[1],1):
        for i in range (0,a.shape[0],1):
            if a[i,j]==1:
                return j
            
def colunadireita(a):
    i=0
    j=a.shape[1]-1
    while j>=0:
        i=0
        while i<=a.shape[0]-1:
            if a[i,j]==1:
                return j
            i=i+1
        j=j-1
        
def linhacima(a):
    for i in range (0,a.shape[0],1):
        for j in range (0,a.shape[1],1):
            if a[i,j]==1:
                return i
                
def linhabaixo(a):
    i=a.shape[0]-1
    j=a.shape[1]-1    
    while i>=0:
        j=a.shape[1]-1
        while j>=0:
            if (a[i,j])==1: #<-------------- O ERRO ESTAVA AQUI!! 
                return i
            j=j-1
        i=i-1
        
linhas=input("digite l: ")
colunas=input("digite c: ")
a=np.zeros((linhas,colunas))
for i in range (0,a.shape[0],1):
    for j in range (0,a.shape[1],1):
        a[i,j]=int(input("Digite um elemento: "))
ce=colunaesquerda(a)
cd=colunadireita(a)
lc=linhacima(a)
lb=linhabaixo(a)
print ce
print cd
print lc
print lb
print (a[lc:lb+1,ce:cd+1])