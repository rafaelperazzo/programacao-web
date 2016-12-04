from __future __import division
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
    

                
            
        
        
        