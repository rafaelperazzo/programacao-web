# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

def slinha(a, x):
    somatorio=0
    for j in range (0, a.shape[1], 1):
        somatorio=somatorio+a[x, j]
    return somatorio
    
def scoluna(a, y):
    somatorio = 0
    for i in range (0, a.shape[0], 1):
        somatorio=somatorio+a[i, y]
    return somatorio

def stotal(a, x, y):
   
    somatorio=slinha(a, x)+scoluna(a, y)-(2*a[x, y])
    return somatorio
    
n=input ("Digite a dimensão da matriz: ")
x=input ("Digite a coordenada i para o peso: ")
y=input ("Digite a coordenada j para o peso: ")


a=np.zeros((n,n))

for i in range (0, a.shape[0],1):
    for j in range (0, a.shape[1], 1):
        a[i,j]=input("Digite um elemente para a matriz: ")
        
s_total=stotal(a, x, y)


print ("%d" %s_total)
