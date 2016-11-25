#ARQUIVO COM SUAS FUNCOES
# -*- coding: utf-8 -*-
from __future__ import division
#CALCULA_PI(M)
def calcula_pi(m):
    soma=0
    i=1
    q=2
    while i<=m:
        if 1<=m and m<=2000:
            if i%2==0:
                soma=soma-(4/(q*(q+1)*(q+2)))
            else:
                soma=soma+(4/(q*(q+1)*(q+2)))
        i=i+1
        q=q+2
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
    
#CALCULA_CO_SEN(z,e)
def calcula_co_sen(z,e):
    i=1
    j=2
    soma=0
    termo+((z**j)/fatorial(j))
    
    while termo>e:
        if i%2!=0:
            soma=soma-termo
        else:
            soma=soma+termo
            
        termo=((z**j)/fatorial(j))
        i=i+1
        j=j+2
        
    cos=1+soma
    return cos
    
#CALCULA_RAZAO_AUREA(m,e)
def calcula_razao_aurea(m,e):
    
    
    operacao=calcula_co_sen((calcula_pi(m))/5,e)
    razao_aurea=2*operacao
    return razao_aurea
    


    
    