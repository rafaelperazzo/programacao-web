# -*- coding: utf-8 -*-
from __future__ import division
import funcoes

#COMECE AQUI
def valorabsoluto(x):
    if x<0:
        x=x*(-1)
    return x
def calcularPi(m):
    j=1
    soma=0
    for i in range(0,m,1):
        soma=soma+ ((-1)**i)*4/((i+1+j)*(i+2+j)*(i+3+j))
        j=j+1
    somaT=soma+3
    return somaT
def calcularcoseno(z,epsilon):
    i=0
    produto=1
    soma=0
    while ((-1)**i)*(z**(2*i))/produto > epsilon:
        produto1=1
        for j in range(1,(2*i + 1), 1):
            produto1=produto1*i
        soma=soma+((-1)**i)*(z**(2*i))/produto1
        i=i+1
        produto=produto1
    return soma
def razaoAurea(m,epsilon):
    piSobre5=calcularPi(m)/5
    cos=calcularcoseno(piSobre5,epsilon)
    razao=2*cos
    return razao
    
    
m=input('Digite o número m de termos da fórmula pi: ')
epsilon=input('Digite o epsilon para o calculo da razão aurea: ')
print('Valor aproximado de pi: %.15f'%calcularPi(m))
print('Valor aproximado da razão aurea: %.15f'%razaoAurea(m,epsilon))