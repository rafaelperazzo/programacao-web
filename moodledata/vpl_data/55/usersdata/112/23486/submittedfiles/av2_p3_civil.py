# -*- coding: utf-8 -*-
from __future__ import division

import numpy as np
n=input('Digite a quandidade de linhas:')
x=input('Digite a coordenada x da localização da torre:')
y=input('Digite a coordenada y da localização da torre:')
a=np.zeros((n,n))
for i in range (0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=input('Digite o termo:')
        
#começo da função 
'''
Para fazer essa atividade eu preferi achar a somatória de todas as linhas e colunas, cololá-las em uma lista
e depois utilizar apenas a soma que me era conveniente.
'''

def locali(a):
    for i in range (0,a.shape[0],1):
        for j in range (0,a.shape[1],1):
            a[x,y]
    return a[x,y]

    
def soma_linha(a):
    s=[]
    for i in range (0,a.shape[0],1):
        soma=0
        for j in range (0,a.shape[1],1):
            soma=soma+a[i,j]
        s.append(soma)
    return  s[x]


def soma_coluna(a):
    s=[]
    for j in range (0,a.shape[1],1):
        soma=0
        for i in range (0,a.shape[0],1):
            soma=soma+a[i,j]
        s.append(soma)
    return s[y]

final=(soma_coluna(a)+soma_linha(a))-(locali(a)*2)
print final