# -*- coding: utf-8 -*-
from __future__ import division
import funcoes
def pi(z): 
    a=2
    b=3
    c=4
    d=4
    e=5
    f=6
    cont=0
    pi=3

    while cont<z:
        pi=pi+((4)/(a*b*c))
        a=a+4
        b=b+4
        c=c+4
        cont=cont+1
        if cont<z:
            pi=pi-((4)/(d*e*f))
            d=d+4
            e=e+4
            f=f+4
            cont=cont+1
    return pi     

def fat(a):
    c=1
    for i in range(1,a+1,1):
        c=c*i
    return c

m=input('Digite o numero m de termos da formula de pi:')
e=input('Digite o epsilon para o calculo da razao aurea:')
resultado=pi(m)
x=resultado/5
i=1
cosx=1

while True:
    termo=((-1)**i)*(x**(2*i))/fat(2*i)
    if ((termo**2)**(1/2))<e:
        break 
    cosx=cosx+termo
    i=i+1

final=2*cosx

print('Valor aproximado de pi: %.15f' %resultado)
print('O valor aproximado da razao aurea e: %.15f' %final)

