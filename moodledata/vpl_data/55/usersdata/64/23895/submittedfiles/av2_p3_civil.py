# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

def slinha(a, b):
    somatorio=0
    for j in range (0, a.shape[1], 1):
        somatorio=somatorio+a[n, j]
    return somatorio
    
def scoluna(a, c):
    somatorio = 0
    for i in range (0, a.shape[0], 1):
        somatorio=somatorio+a[i, c]
    return somatorio

def stotal(a, b, c):
    somatorio = 0
    somatorio=slinha(a, b)+scoluna(a, c)-(2*a[b, c])
    return somatorio
    
n=input ("Digite a dimensão da matriz: ")
b=input ("Digite a coordenada i para o peso: ")
c=input ("Digite a coordenada j para o peso: ")

a=np.zeros((n,n))

for i in range (0, a.shape[0],1):
    for j in range (0, a.shape[1], 1):
        a[i,j]=input("Digite um elemente para a matriz: ")
        
s_total=stotal(a, b, c)
print ("%d" %s_total)
