# -*- coding: utf-8 -*-
from __future__ import division

#COMECE AQUI ABAIXO

#DEFININDO A FUNÇÃO
def congruente(a,b,x0,n,m):
    x=[x0]
    for i in range(0,n,1):
        valor=((a*x[i]+b)%m)/m
        x.append(valor)
    
    return x
    

a=input('Digite a: ')
b=input('Digite b: ')
m=input('Digite m: ')
x0=input('Digite x0: ')
n=input('Digite n: ')


print congruente(a,b,x0,n,m)