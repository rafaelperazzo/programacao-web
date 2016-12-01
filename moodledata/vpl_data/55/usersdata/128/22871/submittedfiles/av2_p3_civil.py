# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

n=input('Insira a dimensão da matriz: ')

x=input('Digite o primeiro índice: ')
y=input('Digite o segundo índice: ')

a=np.zeros((n,n))

soma=0

for i in range (0,n,1):
    soma=soma+a[i,y]

for i in range (0,n,1):
    soma=soma+a[x,i]

soma=soma-(2*a[x,y])

print soma