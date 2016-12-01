# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np


def SomaLinha(a,linha):
    somalinha=0
    for i in range (0,a.shape[1],1):
        somalinha=somalinha+a[linha,j]
    return somalinha
    
def SomaColuna(a,c):
    somacoluna=0
    for i in range(0,a.shape[0],1):
        somacoluna=somacoluna+a[i,c]
    return somacoluna
    
def pesox(a,x,y):
    somatotal=(SomaLinha(a,x)+SomaColuna(a,y))-(2*a[x,y])
    return somatotal
    
n=input('Digite n:')

x=input('Digite x:')
y=input('Digite y:')

a=np.zeros((n,n))
for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=input('Digite os elementos:')
        
peso=pesox(a,x,y)
print ('%d'%peso)