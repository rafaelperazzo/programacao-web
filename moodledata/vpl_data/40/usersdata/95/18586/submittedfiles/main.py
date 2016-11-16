# -*- coding: utf-8 -*-
from __future__ import division
import funcoes

#COMECE AQUI
def fatorial(n):
    produto=1
    for i in range(1,n+1,1):
        produto=produto*i
    return produto

def valor_absoluto(x):
    if x<0:
        x=x*(-1)
    return x

def pi(m):
    soma=0
    j=2
    for i in range(1,m+1,1):
        if i%2==0:
            soma=soma-(4/(j*(j+1)*(j+2)))
        else:
            soma=soma+(4/(j*(j+1)*(j+2)))
        j=j+2
    soma=soma+3
    return soma


def cosseno(z,epsilon):
    iesimo=1
    cosz=1
    i=2
    j=2
    while iesimo>=epsilon:
        if i%2==0:
            cosz=cosz-(z**j)/fatorial(j)
        else:
            cosz=cosz+(z**j)/fatorial(j)
            
        iesimo=valor_absoluto((z**j)/fatorial(j))
        j=j+2
        i=i+1
    return cosz

m=int(input('Digite o número m de termos da fórmula pi:'))
e=input('Digite o epsilon para calcula a razao aurea:')

p=pi(m)
ra=2*(cosseno(pi(m)/5,e))

print('O valor aproximado de pi:%.15f'%p)
print('O valor aproximado da razao aurea:%.15f'%ra)