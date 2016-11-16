# -*- coding: utf-8 -*-
from __future__ import division

#COMECE AQUI ABAIXO

#DEFININDO A FUNÇÃO
def congruente(a,b,x,n,m):
    for i in range(1,n,1):
        x.append=(a*x[i-1])+b

    for i in range(0,len(x), 1):
        n[i]=x[i]/m
    return n

a=input('Digite a: ')
b=input('Digite b: ')
m=input('Digite m: ')
x0=input('Digite x0: ')
n=input('Digite n: ')

x=[x0]

print congruente(a,b,x,n,m)