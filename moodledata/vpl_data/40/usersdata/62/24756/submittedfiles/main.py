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
        

def calcula_co_seno(z, epsilon):
    