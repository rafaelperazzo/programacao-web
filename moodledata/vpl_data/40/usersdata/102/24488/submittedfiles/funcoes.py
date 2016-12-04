from __future__ import division
import numpy as np


def calcula_valor_absoluto(x):
    if x<0:
        x=x*(-1)
        return x 
    else:
        return x
        
        
def cacula_pi(m):
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
        
   
def fatorial(a):
    fatorial=1
    for i in range(1,a+1,1):
        fatorial=fatorial*i
        
    return fatorial
    

def calcula_cos_seno(z,epsilon):
    i=1
    j=2
    soma=0
    termo=((2**j)/fatorial(j))
    while termo>epsilon:
        if i%2!=0:
            soma=soma-termo
        else:
            somaa=soma+termo
            
        i=i+1
        j=j+2
        termo=((2**j)/fatorial(j))
        
        cosseno=1+soma
        return cosseno
    
    
    
    
def calcula_razao_aurea(m,epsilon):
    calcula_razao_aurea=2*(calcula_cos_seno(calcula_pi(m)/5.0,epsilon))

    return razao_aurea
            
       
            
            
        