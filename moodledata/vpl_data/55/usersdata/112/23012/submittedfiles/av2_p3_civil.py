# -*- coding: utf-8 -*-
from __future__ import division

import numpy as np
linhas=input('Digite a quandidade de linhas:')
a=np.zeros((linhas,linhas))
for i in range (0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=input('Digite o termo:')
print a        
x=input('Digite a coordenada x da localização da torre:')
y=input('Digite a coordenada y da localização da torre:')

def soma_linhas(a):
    s=[]
    for i in range (0,a.shape[0],1):
        soma=0
        for j in range (0,a.shape[1],1):
            soma=soma+a[:,j]
            s.append(soma)
    return s
print soma_linhas(a)
    
            