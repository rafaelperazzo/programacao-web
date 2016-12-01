# -*- coding: utf-8 -*-
from __future__ import division
import funcoes

#COMECE AQUI
m=float(input('m: '))
e=input('epsilon: ')
def abs(x):
    return (x**2)**0.5
def pi(m):
    p=3
    i=1
    while i<=m:
        termo= ((-1)**(i+1))*4/(2*i*(2*i+1)*(2*i+2))
        p=p+termo
        i=i+1
    return p
def fat(x):
    soma=1
    for i in range(1,x+1,1):
        soma=soma*i
    return soma
    
def cos(z,epsilon):
    soma=1
    i=1
    while True:
        termo=((-1)**i)*(x**(2*i))/fat(2*i)
        if termo<epsilon:
            break
        soma=soma+termo
    return soma
