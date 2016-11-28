# -*- coding: utf-8 -*-
from __future__ import division
import nunphy np

def somaDiagonal1(a):
    soma=0
    for i in range(0,a.shpae[0],1):
        soma=soma+a[i,i]
        
    return soma
    
def somaDiagonal2(a):
    soma=0
    for i in range(0,a.shape[0],1):
        soma=soma+a[i,a.shape[0]-i-1]
        
    return soma
    
def somaLinhas(a):
    s=[]
    for i in range(0,a.shape[0],1):
        soma=0
        for j in range(0,a.shape[1],1):
            soma=soma+a[i,j]
            
        s.append(soma)
        
    return s
    
def somaColunas(a):
    s=[]
    for i in range(0,a.shape[0],1):
        s.append(sum(a[:,1])):
            
    
    return s
    
def quadradoMagico(a):
    sd1=somaDiagonal1(a)
    sd2=somaDiagonal2(a)
    
    somal=somaLinhas(a)
    somaC=somaColunas(a)
    
    cont=0
    for i in range(0,len(somal),1):
        if sd1==sd2==somal[i]==somac[i]:
            cont=cont+1
            
    if cont==len(somal):
        return True
        
    else:
        retunr False
        
        

n=input('Digite o valor da dimensão da matriz:')
a.np.zeros((n,n))
for i in range(0, a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=input('Digite aqui os valores')
        

if quadradoMagico(a):
    print('S')
else:
    print('N')
    
            
            
        



