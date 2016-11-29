# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

def colesq(a):
    ce = 0
    for i in range(0,a.shape[1],1):
        if 1 in a[:,i]:
            ce = i
            break
    return ce
        
def coldir(a):
    cd = 0
    for i in range(0,a.shape[1],1):
        if 1 in a[:,i]:
            cd = i
    return cd
    
def lincim(a):
    lc = 0
    for i in range(0,a.shape[0],1):
        if 1 in a[i,:]:
            lc = i
            break
    return lc
        
def linbai(a):
    lb = 0
    for i in range(0,a.shape[0],1):
        if 1 in a[i,:]:
            lb = i
    return lb
    
#PROGRAMA PRINCIPAL

linhas = input('Digite a quant de linhas:')
colunas = input('Digite a quant de colunas:')

a = np.zeros((linhas,colunas))

for i in range (0,a.shape[0],1):
    for j in range (0,a.shape[1],1):
        a[i,j] = input('Digite um elemento para a:')

print a[lincim(a):linbai(a),colesq(a):coldir(a)] 
            
            
            

