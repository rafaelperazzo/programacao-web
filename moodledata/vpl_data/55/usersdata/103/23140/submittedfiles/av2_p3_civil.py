# -*- coding: utf-8 -*-
from __future__ import division
linhas=input('Digide a dimensão da matriz:')
x=input('Digite a linha que contém a célula em questão:')
y=input('Digite a coluna que contém a célula em questão:')
a=np.zeros((linhas,linhas))
for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=input('Digite um valor')
somal=0
somac=0
for i in range(0,shape[0],1):
    somal=somal+a[i,y]
for j in ranje(0,shape[1],1):
    somac=somac+a[x,j]
Peso=somac+somal
print Peso