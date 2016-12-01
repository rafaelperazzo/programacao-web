# -*- coding: utf-8 -*-
from __future__ import division
import funcoes

#COMECE AQUI

def calcula_valor_absoluto(x):
    if x<0:
        x=(x*(-1))
        return x
    else:
        return x
        
def calcula_pi(m):
    soma=0
    d=2
    i=1
    while i<=m: #Tinha um erro aqui!!
        if i%2==0:
            soma=(soma-(4/((d)*(d+1)*(d+2))))
        else:
            soma=(soma+(4/((d)*(d+1)*(d+2))))
        i=(i)+1
        d=(d)+2
    pi=3+(soma)
    return pi

def fatorial(f):
    i=1
    fatorial=1
    while i<=f:
        fatorial=(fatorial)*i
        i=i+1
    return fatorial
    
def calcula_co_seno(z,e):
    soma=0
    i=1
    n=2
    cosx=((z**n)/(fatorial(n)))
    while cosx>e:
        if i%2==0:
            soma=soma-cosx
        else:
            soma=soma+cosx
        i=i+1
        n=n+2
        cosx=((z**n)/(fatorial(n)))
    coseno=1+(soma)
    return coseno
    
def calcula_razao_aurea(m,e):
    calculo=calcula_co_seno(calcula_pi(m)/5,e)
    razaoAurea=2*(calculo)
    return razaoAurea
    
m=input('digite o numero m de termos da formula de pi:')
e=input('digite o epsilon para o calculo da razao aurea:')

print('%.15f'%(calcula_pi(m)))
print calcula_co_seno(calcula_pi(m),0.000001)
print('%.15f'%(calcula_razao_aurea(m,e)))
