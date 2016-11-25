# -*- coding: utf-8 -*-
from __future__ import division
#ARQUIVO COM SUAS FUNCOES
#DEFININDO FUNÇÃO PARA O VALOR ABSOLUTO DE X
def modulo(x):
    if x<0:
        x=x*(-1)
    else:
        x=x
    return x
    
#DEFININDO FUNÇÃO PARA CÁLCULO DO FATORIAL
def fatorial(x):
    fat=1
    for i in range (2,x+1,1):
        fat=fat*i
    return fat

#DEFININDO FUNÇÃO PARA CÁLCULO DO COSSENO
def cos(x,e):
    x=modulo(x)
    soma=1
    i=1
    while True:
        u=2*i
        if ((x**u)/(fatorial(u)))<=e:
            break
        if (i%2)==0:
            soma=soma+((x**u)/(fatorial(u)))
        elif (i%2)!=0:
            soma=soma-((x**u)/(fatorial(u)))
        i=i+1
    return soma
    
#DEFININDO FUNÇÃO PARA CÁLCULO DE PI
def pi(m):
    i=1
    soma=3
    cont=0
    while cont<m:
        u=2*i
        if (i%2)==0:
            soma=soma-(4/(u*(u+1)*(u+2)))
            cont=cont+1
        elif (i%2)!=0:
            soma=soma+(4/(u*(u+1)*(u+2)))
            cont=cont+1
        i=i+1
    return soma