# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 19:12:16 2016

@author: Jonathan Moreira
"""

from __future__ import division

#CALCULA_PI(M)
def calcula_pi(m):
    soma=0
    digito=2
    i=1

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

#CALCULA_VALOR_ABSOLUTO(x)
def calcula_valor_absoluto(x):
    
    if x<0:
        x=x*(-1)
        return x
    
    else:
        return x
        
#FATORIAL(n)
def fatorial(n):
    i=1
    fatorial=1

    while i<=n:
        fatorial=fatorial*i
        i=i+1
    
    return fatorial

#CALCULA_COS_SEN(z,e)
def calcula_cos_sen(z,e):
    soma=0
    j=2
    i=1
    termo=((z**j)/fatorial(j))

    while termo>e:
        if i%2!=0:
            soma=soma-termo
        else:
                soma=soma+termo
                
        termo=((z**j)/fatorial(j))  
        j=j+2
        i=i+1
    
    cos=1+soma
    return cos

#CALCULA_RAZAO_AUREA(m,e)
def calcula_razao_aurea(m,e):
    
    operacao=calcula_cos_sen((calcula_pi(m))/5,e)
    r_aurea=2*operacao
    
    return r_aurea
