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
    for i in range (0,a.shape[0],1):
        soma=0
        for j in range (0,a.shape[1],1):
            soma=soma+a[i,j]
        s.append(soma)
        for t in range(0,len(s)-1,1):
            c=s[y+1]
    return  c
print soma_linha(a)

def soma_coluna(a):
    s=[]
    for j in range (0,a.shape[1],1):
        soma=0
        for i in range (0,a.shape[0],1):
            soma=soma+a[i,j]
        s.append(soma)
        for t in range (0,len(s)-1,1):
            c=s[x+1]
    return c
print soma_coluna(a)

final=soma_coluna(a)+soma_linha(a)-(2*locali(a))

print final
                        