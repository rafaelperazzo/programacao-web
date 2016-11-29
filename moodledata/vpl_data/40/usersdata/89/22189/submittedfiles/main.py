# -*- coding: utf-8 -*-
from __future__ import division
import funcoes

#COMECE AQUI

def calcula_valor_absoluto(x):
    if x<0:
        x=x*(-1)
    else:
        x=x*1
    
    return x
    
def calcula_pi(m):
    soma=0
    denominador=2
    termo=1
    
    while termo<=m:
        if termo%2==1:
            soma=soma+4/((denominador)*(denominador+1)*(denominador+2))
        else:
            soma=soma-4/((denominador)*(denominador+1)*(denominador+2))
            
        denominador=denominador+2
        termo=termo+1
    pi=3+(soma)
        
    return pi
        
def fatorial(n):
    i=1
    fatorial=1
    while i<=n: #AQUI É MENOR OU IGUAL
        fatorial=fatorial*i
        i=i+1
        
    return fatorial
    
def calcula_co_seno(z,epsilon):
    expoente=2
    termo=((z**expoente)/(fatorial(expoente))) 
    i=1
    soma=0

    while termo > epsilon:
        if i%2==1:
            soma=soma-termo
        else:
            soma=soma+termo
        
        i=i+1
        expoente=expoente+2
        termo=((z**expoente)/(fatorial(expoente)))
        
    cosseno= 1+(soma) 
    
    return cosseno
    
def calcula_razao_aurea(m,epsilon):
    formula=calcula_co_seno(calcula_pi(m)/5,epsilon)  
    
    razaoaurea=2*(formula)
    
    return razaoaurea
    
#programa principal

m=input('digite o numero m de termos da formula pi:')
epsilon=input('digite o epsilon para o calculo da razao aurea:')

print('%.15f'% (calcula_pi(m)))
print('%.15f'% (calcula_razao_aurea(m,epsilon)))