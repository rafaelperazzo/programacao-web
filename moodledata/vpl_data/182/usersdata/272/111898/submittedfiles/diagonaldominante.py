# -*- coding: utf-8 -*-
import numpy as np

n=int(input('Digite a ordem da matriz: '))
a=np.zeros( (n,n) )
for i in range (0,a.shape[0],1):
    for j in range (0,a.shape[1],1):
        a[i,j]=float(input('Digite um valor: '))

print(a)