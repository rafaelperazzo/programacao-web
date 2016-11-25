# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

def magico(x):
    
    cont=0
    a=[]
    for i in range(0, x.shape[1], 1):
        a.append(x[0,i])
    soma= sum(a)
    
    for i in range(1, x.shape[0], 1):
        somal=0
        for j in range(0, x.shape[1], 1):
            somal=somal+ x[i,j]
    if somal!=soma:
        cont= cont+1
    
    for i in range(0, x.shape[1], 1):
        somac=0
        for j in range(0, x.shape[0], 1):
            somac=somac+ x[j,i]
    if somac!=soma:
        cont= cont+1
        
    somadp=0
    for i in range(0, x.shape[0], 1):
        somadp=somadp+ x[i,i]
    if somadp!=soma:
        cont=cont+1
    
    somads=0
    for i in range(0, x.shape[0], 1):
        somads=somads+ x[i,(x.shape[1]-1)-i]
    if somads!=soma:
        cont=cont+1
    
    if cont==0:
        return True
    else:
        return False

linhas= int(input('Digite o numero de linhas:  '))
colunas= int(input('Digite o numero de colunas:  '))

x= np.zeros((linhas, colunas))
for i in range(0, linhas, 1):
    for j in range(0, colunas, 1):
        x[i,j]= input('Digite um valor da matriz: ')

if magico(x):
    print 'S'
else:
    print 'N'