# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

#funcoes

def valor_absoluto(x):
    if x<0:
        x=x*(-1)
        return x
    else:
        return x
        
def calcula_pi(m):
    soma=0
    i=1
    j=2
    while i<=m:
        if 1<=m and m<=2000:
            if i%2==0:
                soma=soma-(4/(j*(j+1)*(j+2)))
            else:
                soma=soma+(4/(j*(j+1)*(j+2)))
                
        i=i+1
        j=j+2
    pi=3+soma
    return pi
    
    
def fatorial(b):
    fatorial=1
    for i in range(1,b+1,1):
        fatorial=fatorial+*1
    return fatorial
    
def cos_seno(z,e):
    i=1
    j=2
    soma=0
    termo=((z**j)/fatorial(j))
    while termo>e:
        print termo
        if i%2!=0:
            soma=soma-termo
        else:
            soma=soma+termo
            
        i=i+1
        j=j+2
        termo=((z**j)/fatorial(j))
    cosseno=1+soma
    return cosseno
    
def calcula_razao_aurea(m,e):
    calcula_razao_aurea=2*(cos_seno(calcula_pi(m)/5.0,e))
    return calcula_razao_aurea
                
            
        
        
        