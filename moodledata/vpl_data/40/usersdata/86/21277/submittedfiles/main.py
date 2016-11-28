# -*- coding: utf-8 -*-
from __future__ import division
import funcoes

#COMECE AQUI

def calcula_pi(x):
    cont=1
    e=2
    pi=0
    while cont<=x:
        if cont%2==0:
            pi=pi-(4/((e)*(e+1)*(e+2)))
        else:
            pi=pi+(4/((e)*(e+1)*(e+2)))
    cont=cont+1
    e=e+2
    return (pi+3)

def calcula_valor_absoluto(w):
    if w>=0:
        return w
    else:
        return w*(-1)

def calcula_co_seno(x,epsilon):
    cont=1
    cosx=0
    d=200
    f=2
    while d>=epsilon:
        fact=1
        for j in range(1,f+1,1):
            fact=fact*j
        if cont%2==1:
            cosx=coxs-((x**f)/fact)
        else:
            cosx=coxs+((x**f)/fact)
        d=((x**f)/fact)
        cont=cont+1
        f=f+2
    return (cosx+1)

def calcula_razao_aurea(x,epsilon):
    fi=2*calcula_co_seno(x,epsilon)
    return fi

m=int(input('quantidade m de termos:'))
ep= input('epsilon:')

print (calcula_pi(m))
print (calcula_razao_aurea(m,ep))
    
