# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

def colunaE(a):
    colEsquerda=0
    for j in range(0,a.shape[1],1):
        for i in range (0,a.shape[0],1):
            if a[i,j]==1:
                return j #<------------- O ERRO ESTAVA AQUI! O break só para uma repetição!!
                
def colunaD(a):
    colDireita=0
    j=a.shape[1]-1
    i=a.shape[0]-1
    while j>=0:
        while i>=0:
            if a[i,j]==1:
                return j #<------------- O ERRO ESTAVA AQUI! O break só para uma repetição!!
            i=i-1
        j=j-1

def linhaC(a):
    linhaCima=0
    for i in range(0,a.shape[0],1):
        for j in range (0,a.shape[1],1):
            if a[i,j]==1:
                return i #<------------- O ERRO ESTAVA AQUI! O break só para uma repetição!!

def linhaB(a):
    linhaBaixo=0
    j=a.shape[1]-1
    i=a.shape[0]-1
    while i>=0:
        while j>=0:
            print a[i,j]
            if a[i,j]==1:
                print i 
                print ('Entrou')
                return i #<------------- O ERRO ESTAVA AQUI! O break só para uma repetição!!
            j=j-1
        i=i-1
    
n=input('Insira a quantidade de linhas:')
m=input('Insira a quantidade de colunas:')
a=np.zeros((n,m))
for i in range(0,a.shape[0],1):
    for j in range (0,a.shape[1],1):
        a[i,j]=input('Insira um valor:')
l=linhaC(a)
print l
f=linhaB(a)+1 
print f
d=colunaE(a)
print d
c=colunaD(a)+1
print c
print(a[l:f,d:c])