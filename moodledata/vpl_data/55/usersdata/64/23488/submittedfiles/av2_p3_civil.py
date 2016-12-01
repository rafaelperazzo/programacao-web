# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

n=input ("Digite a dimensão da matriz: ")
a=input ("Digite a coordenada i para o peso: ")
b=input ("Digite a coordenada j para o peso: ")

linha = n
coluna = n
c=np.zeros((linha,coluna))

for i in range (0, a.shape[0],1):
    for j in range (0, a.shape[1], 1):
        a[i,j]=input("Digite um elemente para a matriz: ")
        
x=[]
for i in range (0, a.shape[0],1):
    if i=a:
        x.append=a[i,j]
