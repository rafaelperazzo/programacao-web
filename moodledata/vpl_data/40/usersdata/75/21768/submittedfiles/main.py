# -*- coding: utf-8 -*-
from __future__ import division
import funcoes


def calcula_valor_abssoluto(x):
    if x<0:
        x=x*(-1)
        return x
    else:
        return x
        
x=input('Digite o valor de x:')

print (calcula_valor_abssoluto(x))
    
def calcula_pi(m):
    soma=0
    i=1
    denominador=2
    while i<=m:
        if (m>=1) and (m<=2000):
            if i%2!=0:
                soma=soma+4/(denominador*(denominador+1)*(denominador+2))
            else:
                soma=soma-4/(denominador*(denominador+1)*(denominador+2))
        i=i+1
        denominador=denominador+2
        
    pi=3+soma
        
    return pi
    
m=input('Digite o valor de m:')

print (calcula_pi(m))
    
def fatorial(n):
    i=1
    fatorial=1
    while i<=n:
        fatorial=fatorial*i
        i=i+1
        
    return fatorial 
    
def co_seno(z,epsilon):
    soma=0
    expoente=2
    termo=((z**expoente)/fatorial(expoente))
    i=1
    while termo>epsilon:
        if i%2!=0:
            soma=soma-termo
        else:
             soma=soma+termo
        expoente=expoente+2
        i=i+1
        
    cos=soma+1
    
    return cos
    
epsilon=input('Digite o valor de epsilon:')
z=input('Digite o valor de z:')

print co_seno(z,epsilon)

def razao_Aurea(m,epsilon):
    pi=calcula_pi(m)/5

    razao_aurea=2*co_seno(pi,epsilon)
