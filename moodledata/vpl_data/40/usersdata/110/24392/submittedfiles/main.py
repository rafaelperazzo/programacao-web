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
m=input('Digite m: ')
print(calculatPi(m))