# -*- coding: utf-8 -*-
from __future__ import division
import funcoes

#COMECE AQUI
m=input("digite a quantidade de termos de pi")
epsilon=input("digite os valor para o calculoda razao aurea")
def modulo (x):
    if x>=0:
        x=x*1
        
    else:
        x=(-1)*x
    return x
def pi (m):
    soma=0
    denom=2
    termo=1
    whlile m<=2000:
        if m%2==1:
            soma=soma + (4/(denom)*(denom +1) *(denom +2))
        else:
            soma=soma -(4/(denom)*(denom+1)*(denom+2))
        pi=3+soma
    return pi

def fatorial (numero):
    a=1
    b=2
    while b<=numero:
        a=a*b
        b=b+1
        
    return vetorial 

        
            