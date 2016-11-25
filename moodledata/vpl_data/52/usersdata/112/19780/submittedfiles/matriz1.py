# -*- coding: utf-8 -*-
from __future__ import division

import numpy as np
linhas=input('Digite a quantidade de linhas:')
colunas=input('Digite a quantidade de linhas:')
a=np.zeros((linhas,colunas))
for i in range (0,a.shape[0],1):
    for j in range (1,a.shape[0],1):
        a[i,j]=input('Digite o elementos:')
def primeira linha(lista):
    for i in range(0,len(a),1):
        if a[i]==1:
            return a[i]
def ultima linha(lista):
    for j in range (a[i],len(a),1):
        if a[j]==1:
            return a[j]
if primeira linha(a):
    print (a[i])
if ultima linha(a):
    print (a[j])
    
    
    
    
    

a=[]
for i in range(0,linhas,1):
    a.append(input('Digite o elemento da lista))