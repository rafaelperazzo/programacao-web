# -*- coding: utf-8 -*-
from __future__ import division
import funcoes
def fatorial(z):
    produto=1
    for i in range(1,len(z),1):
        produto=produto*z[i]
    return produto
    
def calcula_co_seno(z,y):
    y=2
    soma=0
    for i in range(1,len(x)+1,1):
        if i%2==0:
            soma=soma+(x**y)/fatorial
        else:soma=soma-(x**y)/fatorial
    y=y+2    
#COMECE AQUI
