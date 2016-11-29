# -*- coding: utf-8 -*-
from __future__ import division
import funcoes

#COMECE AQUI

m = input('Digite o numero m de termos de pi:')
epsilon = input('Digite o epsilon para o calculo da razao aurea:')

def calcula_valor_absoluto(x):
    if x>=0:
        x=x*1
    else:
        x=x*(-1)
        
    return x
    
def calcula_pi(m):
    soma = 0
    den = 2
    termo = 1
    while 1<=m<=2000:
        if m%2==1:
            soma = soma + (4/(den)*(den + 1)*(den + 2))
        else:
            soma = soma - (4/(den)*(den + 1)*(den + 2))
    pi = 3 + soma
    return pi
    
def calcula_co_seno(z, epsilon):