# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

def qMagico(m):
    
    cont1=0
    
    for i in range (0,m.shape[0]-1,1):
        if sum(m[i,:])==sum(m[i+1,:]):
            cont1=cont1+1
            
    if cont1==m.shape[0]:
        somaLinhas=sum(m[0,:])


    cont2=0
    
    for j in range (0,m.shape[1]-1,1):
        if sum(m[:,j])==sum(m[:,j]):
            cont2=cont2+1
            
    if cont2==m.shape[1]:
        somaColunas=sum(m[:,0])
        
    

    cont3=0
    somaD1=0
    for k in range(0,m.shape[0],1):
        somaD1=somaD1+m[k,k]
        cont3=cont3+1
    
    if cont3==m.shape[0]:
        somaDiagonal1=somaD1
        


    cont4=0
    somaD2=0
    j=m.shape[1]-1
    i=0
    
    while True:
        somaD2=somaD2+m[i,j]
        cont4=cont4+1
        
        j=j-1
        i=i+1
        
        if cont4==m.shape[0]:
            break
            somaDiagonal2=somaD2
            
    
    if somaLinhas==somaColunas and somaColunas==somaDiagonal1 and somaDiagonal1==somaDiagonal2:
        return True
    else:
        return False

n=input('Dimensão da matriz: ')
m=np.zeros((n,n))

for i in range (0,m.shape[0],1):
    for j in range (0,m.shape[1],1):
        m[i,j]=input('Digite um termo: ')

if qMagico(m):
    print 'SIM'
else:
    print 'NÃO'