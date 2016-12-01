# -*- coding: utf-8 -*-
from __future__ import division
def somadiagonal1(a):
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
    s=[]
    for i in range(0,a.shape[0],1):
        soma=0
        for i in range(0,a.shape[1],1):
            soma=soma+a[i,j]
        s.append(soma)
    
    return s
    
def somaColunas(a):
    s=[]
    n=a.shape[0]
    for i in range(0,n,1):
        s.append(sum(a[:,i]))
    
    return s
    
def quadradoMagico(a):
    sd1= somaDiagonal1(a)
    sd2= somaDiagonal2(a)
    
    somaL= somaLinhas(a)
    somac= somaColunas(a)
    
    cont=0
    for i in range(0,len(somaL,1):
        if sd1==sd2==somaL[i]==somaC[i]:
            cont=cont+1
        
    if cont == len(somaL):
        return True
    else:
        return False