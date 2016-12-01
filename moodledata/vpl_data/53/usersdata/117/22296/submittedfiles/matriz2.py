# -*- coding: utf-8 -*-
from __future__ import division

def somaDiagonal1(a):
    soma=0
    for i in range (0,a.shape[0],1):
        soma=soma+a[i,j]
        
    return soma
    
    
def somaDiagonal2(a):
    soma=0
    for i in range (0,a.shape[0],1):
        soma=soma+a[i,a.shape[0]-i-1]
        
    return soma
    
def somaLinhas(a):
    s=[]
    n=a.shape[0]
    for i in range (0,n,1):
        s.append(sum(a[i,:]))
    return s
    
def somaColunas(a):
    s=[]
    n=a.shape[0]
    for i in range (0,n,1):
        s.append(sum(a[:,i]))
    return s
            
def quadradomagico(a):
    sd1=somaDiagonal1(a)
    sd2=somaDiagonal2(a)
    
    somaL=somaLinhas(a)
    somaC=somaColunas(a)
    
    cont=0
    for i in range (0,len(somaL),1):
    if sd1==sd2==somaL[i]==somaC[i]:
        cont=cont+1
        
    if cont==len(somaL):
        return True
    else:
        return False
        
if quadradomagico(a):
    print ('S')
else:
    print ('N')
        

