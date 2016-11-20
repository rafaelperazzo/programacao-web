#ARQUIVO COM SUAS FUNCOES
# -*- coding: utf-8 -*-
from __future__ import division
#CALCULA_PI(M)
def calcula_pi(m):
    soma=0
    i=1
    digito=2
    while i<=m:
        if 1<=m and m<=2000:
            if i%2==0:
                soma=soma-(4/(digito*(digito+1)*(digito+2)))
            else:
                soma=soma+(4/(digito*(digito+1)*(digito+2)))
        i=i+1
        digito=digito+2
    pi=3+soma
    return pi
    
#CALCULA_VALOR_ABSOLUTO(X)
def calcula_valor_absoluto(x):
    
    if x<0:
        x=x*(-1)
        return x
    else:
        return x
        
#FATORIAL(n)
def fatorial(n):
    fatorial=1
    i=1
    
    while i<=n:
        fatorial=fatorial*i
        i=i+1
    return fatorial    

    
    