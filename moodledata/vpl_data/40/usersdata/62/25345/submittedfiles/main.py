# -*- coding: utf-8 -*-
from __future__ import division
import funcoes

#COMECE AQUI

def calcula_valor_absoluto(x):
    if x<0:
        x=x*(-1)
    else:
        x=x
    return x
    
def calcula_pi(m):

    i=1   
    soma=0
    denominador=2
    if 1<=m<=2000:
        while i<=m:
            if i%2!=0:
                soma=soma+(4/(denominador*(denominador+1)*(denominador+2)))
            else:
                soma=soma-(4/(denominador*(denominador+1)*(denominador+2)))
            i=i+1
            denominador=denominador+2
        
        pi=3+soma
        return pi

def fat(n):
    i=1
    fat=1
    while i<=n:
        fat=fat*i
        i=i+1

def calcula_co_seno(x, epsilon):
    soma=0
    exp=2
    t=((x**exp)/fat(exp))
    i=1
    while t>epsilon:
        t=((x**exp)/fat(exp))
        if i%2!=0:
            soma=soma-t
        else:
            soma=soma+t
        exp=exp+2
        i=i+1
        
    coseno=soma+1
    
    return coseno
    
def razao_Aurea(m,epsilon):

    pi=calcula_pi(m)/5
    razao_Aurea=2*calcula_co_seno(pi, epsilon)
    
    return razao_Aurea
    
m=input('Digite o valor de m: ')
epsilon=input('Digite o valor de epsilon: ')
razao=razao_Aurea(m,epsilon)

print ('%.15f'%calcula_pi(m))
print ('%.15f'%razao)