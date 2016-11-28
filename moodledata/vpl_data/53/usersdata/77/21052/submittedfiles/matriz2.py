# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

def somaDiagonal1(a):
    soma=0
    for i in range(0,a.shape[0],1):
        soma=soma+a[i,i]
        
    return soma
    
def somaDiagonal2(a):
    soma=0
    for i in range(0,a.shape[0],1):
        soma=soma+a[i,a.shape[0]-i-1]
        
    return soma
    
def somaLinhas(a):
    soma=[]
    for i in range(0,a.shape[0],1):
        soma.append(sum(a[i,:]))
        
    return soma
    
def somaColunas(a):
    soma=[]
    for i in range(0,a.shape[0],1):
        soma.append(sum(a[:,1]))
            
    return soma
    
def quadradoMagico(a):
    sd1=somaDiagonal1(a)
    sd2=somaDiagonal2(a)
    
    somal=somaLinhas(a)
    somaC=somaColunas(a)
    
    cont=0
    for i in range(0,len(somal),1):
        if sd1==sd2==somal[i]==somaC[i]:
            cont=cont+1
            
    if cont==len(somal):
        return True
        
    else:
        return False
        
        

n=int(input('Digite o valor da dimensão da matriz:'))

a=np.zeros((n,n))

for i in range(0, a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=input('Digite aqui os valores')
        

if quadradoMagico(a):
    print('S')
else:
    print('N')
    
            
            
        



