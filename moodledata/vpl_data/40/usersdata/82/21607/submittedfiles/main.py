# -*- coding: utf-8 -*-
from __future__ import division
import funcoes

m = input ('Digite o valor de m:')
soma=3
den=2
termo=1

def pi(m):
   
    for i in range (0,m,1):
        soma = soma + (4/(den*(den+1)*(den+2)))
    den=den+1
    termo=termo+1
    
    print (soma)


    



