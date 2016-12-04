# -*- coding: utf-8 -*-
from __future__ import division
import funcoes

def calcula_valor_absoluto(x):
    if x<0:
        x*(-1)
    return x
    
def fatorial(z, epsilon):
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
print('valor aproximado de pi: %.15f' %calcula_pi(m))

z=calcula_pi(m)
m = input('Digite o valor de m:')
epsilon = input ('Digite o valor de epsilon:')

def calcula_co_seno(z, epsilon):
    exp=2
    soma=0
    i=1
    termo=1
    
    while True:  
        if termo>=epsilon:
            if i%2==0:
                soma=soma-termo
            else:
                soma=soma+termo
                
            if termo<epsilon:
                break
                exp=exp+2
                termo=(calcula_valor_absoluto(((z)**exp)/fatorial(exp)))
                i=i+1
                
    return soma
    
def calcula_razao_aurea(m, epsilon):
    
    razao = 2*(calcula_co_seno(pi(m)/5,epsilon))
    return razao
    
    print ('%.15f'%calcula_razao_aurea)
    
    
    
    
    
    



    



