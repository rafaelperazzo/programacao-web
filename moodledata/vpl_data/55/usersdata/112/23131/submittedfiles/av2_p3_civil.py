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

def locali(a):
    for i in range (0,a.shape[0],1):
        for j in range (0,a.shape[1],1):
            a[x,y]
    return a[x,y]
print locali(a)
    
def soma_linha(a):
    s=[]
    soma=0
    for i in range (0,a.shape[0],1):
        for j in range (0,a.shape[1],1):
            if a[i,j]==a[:,y]:
                s.append(a[i,j])
    return s 
print soma_linha(a)
            