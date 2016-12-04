 # -*- coding: utf-8 -*-
from __future__ import division
import funcoes

def calcula_pi(x):
    cont=1
    i=2
    pi=0
    while cont<=x:
        if cont%2==0:
            pi=pi-(4/((i)*(i+1)*(i+2)))
        else:
            pi=pi+(4/((i)*(i+1)*(i+2)))
        cont=cont+1
        i=i+2
    return (pi+3)

def calcula_valor_absoluto(x):
    if x>=0:
        return x
    else:
        return x*(-1)

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
            cosx=cosx-((x**f)/fact)
        else:
            cosx=cosx+((x**f)/fact)
        d=calcula_valor_absoluto((x**f)/fact)
        cont=cont+1
        f=f+2
    return (cosx+1)

def calcula_razao_aurea(x,epsilon):
    fi=2*calcula_co_seno((calcula_pi(x)/5),epsilon)
    return fi

m=int(input('quantidade m de termos:'))
ep= input('epsilon:')

print ('%.15f'%calcula_pi(m))
print ('%.15f'%calcula_razao_aurea(m,ep))

