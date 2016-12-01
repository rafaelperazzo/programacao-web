# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np 

#Entrada 

n = int(input('insira a dimensão do tabuleiro:'))

x = int(input('insira o valor da primeira coordenada:'))
y = int(input('insira o valor da segunda coordenada:'))

a=np.zeros ((n,n))

for i in range (0,a.shape[0],1):
    for j in range (0,a.shape[1],1):
        a[i,j]=int(input('insira um valor:'))

i=x
cont=0
for j in range (0,a.shape[1],1):
    if j!=y:
        cont=cont+a[i,j]

j=y
cont2=0
for i in range (0,a.shape[0],1):
    if i!=x:
        cont2=cont2+a[i,j]

peso=cont+cont2

print peso 


