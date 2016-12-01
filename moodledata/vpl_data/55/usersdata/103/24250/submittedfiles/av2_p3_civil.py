# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np
linhas=input('Digide a dimensão da matriz:')
colunas=linhas
x=input('Digite a linha que contém a célula em questão:')
y=input('Digite a coluna que contém a célula em questão:')
a=np.zeros((linhas,colunas))
for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=input('Digite um valor:')
somal=0
somac=0
for i in range(0,a.shape[0],1):
    somal=somal+a[i,y]
for j in range(0,a.shape[1],1):
    somac=somac+a[x,j]
somal=somal-a[x,y]
somac=somac-a[x,y]
Peso=somac+somal
print int(Peso)