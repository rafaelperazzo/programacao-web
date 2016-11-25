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
    while m<=2000: #TINHA UM ERRO AQUI
        if m%2==1:
            soma=soma + (4/(denom)*(denom +1) *(denom +2))
        else:
            soma=soma -(4/(denom)*(denom+1)*(denom+2))
    pi=3+soma #tinha um erro aqui
    return pi

def fatorial (numero):
    a=1
    b=2
    while b<=numero:
        a=a*b
        b=b+1
        
    return a #TINHA UM ERRO AQUI!!

        
def coseno(z,e):
    soma=0
    j=2
    i=1
    termo=((z**j)/fatorial(j))
    while termo>e:
        if i%2==0:
            soma=soma - termo
        else:
            soma=soma + termo
        j=j+2
        i=i+1
        cos=1+soma
        return cos
    def razao_aurea (m,e):
        razao=(2*cos)*(pi/5)
        return razao
        
print ("%.15f" %pi (m))
print("%.15f" %razao_aurea)