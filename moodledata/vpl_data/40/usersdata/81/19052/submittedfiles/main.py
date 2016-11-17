# -*- coding: utf-8 -*-
from __future__ import division
import funcoes

m=int(input('Digite m:'))
e=input('Digite o epsilon para o cosseno:')

def fatorial(n):
    n_fat=1
    for i in range(1,n+1,1):
        n_fat*=n
        return n_fat

def calcula_valor_absoluto(x):
    if x<0:
        x=x*(-1)
    return x

def pi(m):    
    soma=0
    j=2
    for i in range (1,m+1,1):
        if i%2==0:
            soma=soma-(4/(j*(j+1)*(j+2)))
        else:
            soma=soma+(4/(j*(j+1)*(j+2)))
        j=j+2    
    pi=3+soma
    return pi
    

print ('%.15f' %pi(m))

def calcula_co_seno(z,epsilon):
    soma_cos=0
    j=2
    i=1
    while True:
        termo = (((pi/5)**j)/fatorial(j))
        if i%2!=0:
            soma_cos=soma_cos+termo
        else:
            soma_cos=soma_cos-termo
        j=j+2
        i=i+1
        if termo<epsilon:
            break
    
        cosseno=1-soma_cos
        return cosseno

def calcula_razao_aurea(m,epsilon):
    razao= 2*calcula_co_seno(m,epsilon)
    return razao

print ('%.15f' %calcula_razao_aurea(m,e))