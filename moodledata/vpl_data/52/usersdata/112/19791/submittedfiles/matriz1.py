# -*- coding: utf-8 -*-
from __future__ import division

import numpy as np
linhas=input('Digite a quantidade de linhas:')
colunas=input('Digite a quantidade de linhas:')
a=np.zeros((linhas,colunas))
for i in range (0,a.shape[0],1):
    for j in range (1,a.shape[0],1):
        a[i,j]=input('Digite o elementos:')
        
def primeiralinha(lista):
    for i in range(0,len(a),1):
        if a[i]==1:
            return a[i]

print primeiralinha(a)
    
    
    
    
    

a=[]
for i in range(0,linhas,1):
    a.append(input('Digite o elemento da lista'))
        