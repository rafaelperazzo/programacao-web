# -*- coding: utf-8 -*-
from __future__ import division

import numpy as np
ln=input("digite o numero de linhas e colunas: ")
a=np.zeros((ln,ln))
b=np.zeros((ln,ln))
for i in range(0,a.shape[0]):
    for j in range(0,b.shape[0]):
        a[i,j]=input("coloca o numero: ")
print a