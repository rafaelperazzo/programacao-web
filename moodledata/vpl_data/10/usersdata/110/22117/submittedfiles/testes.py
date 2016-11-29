# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np
def linhacima(a):
    linhaC=0
    for i in range(0,a.shape[0],1):
        if 1 in a[i,:]:
          linhaC=i
          break
    return linhaC
def linhabaixo(a):
    linhaB=0
    for i in range(0,a.shape[0],1):
        if 1 in a[i,:]:
          linhaB=i
    return linhaB
def colunaesq(a):
    colunaE=0
    for i in range(0,a.shape[1],1):
        if 1 in a[:,i]:
          colunaE=i
          break
    return colunaE
def colunadir(a):
    colunaD=0
    for i in range(0,a.shape[1],1):
        if 1 in a[:,i]:
          colunaD=i
    return colunaD   
linhas=input('Digite linhas: ')
c=input('Digite colunas :' )
a=np.zeros((linhas,c))
for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=input('Digite valor: ')
print(a[linhacima(a):linhabaixo(a)+1 ,colunaesq(a):colunadir(a)+1] )