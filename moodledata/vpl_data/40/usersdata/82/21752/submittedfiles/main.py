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
    soma=0
    den=2
    for i in range (1,m+1,1):
        if i%2==0:
            soma = soma-(4/(den*(den+1)*(den+2)))
        else:
            soma = soma+(4/(den*(den+1)*(den+2)))
        
        den=den+2
    
    soma=soma+3
    return soma
print('valor aproximado de pi: %.15f' %clacula_pi(m))
    
    
    
    
    



    



