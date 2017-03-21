# -*- coding: utf-8 -*-
from __future__ import division

import numpy as np
ln=input("digite o numero de linhas e colunas: ")
a=np.zeros((ln,ln))
b=np.zeros((ln,ln))
for i in range(0,a.shape[0]):
    for j in range(0,b.shape[0]):
        a[i,j]=input("coloca o numero: ")
for k in range(0,b.shape[0]):
    for l in range(0,b.shape[1]):
        b[l,k]=a[k,l]
print b
print a