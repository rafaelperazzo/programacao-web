# -*- coding: utf-8 -*-
from __future__ import division
import funcoes

def calcula_valor_absoluto(x):
    if x<0:
        x*(-1)
    return x
    
def calcula_co_seno(z,epsilon):
    produto=1
    for i in range (1,n+1,1):
        produto = produto*i
    return produto
    
    
m = input('Digite o valor de m:')

def calcula_pi(m):
    soma=3
    den=2
    termo=0
    
    for i in range (0,m,1):
        if termo%2==0:
            soma = soma + (4/(den*(den+1)*(den+2)))
        else:
            soma = soma - (4/(den*(den+1)*(den+2)))
    
        den=den+2
        termo=termo+1
    return soma
    
        den=den+2
        termo=termo+1
    return soma
    
    



    



