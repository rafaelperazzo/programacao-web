# -*- coding: utf-8 -*-
#ARQUIVO COM SUAS FUNCOES
from __future__ import division #<------------------FALTAVA ESTA LINHA
def pi(a):
    pii=0
    c=-1 # c controla o sinal da função
    j=2    
    for i in range(0,a,1):
        b=(4/(j*(j+1)*(j+2)))
        c=(c*(-1))
        b=(b*c)
        pii=pii+b
        j=j+2
    pii=pii+3
    return pii
    
def cos(x,e):
    c=0
    cont=0
    n=2
    while True:
        #Calculando o fatorial
        fatorial=1
        for i in range (n,0,-1):
            fatorial=(i*fatorial)
             
        #Calculando os termos da fórmula termo=''t''
        t=((x**n)/(fatorial))
        c=c+1
        if c%2 != 0:
            cont=cont-t
        else:
            cont=cont+t
        #Atualizando
        n=n+2
        if t<=e:
            break
    cos=cont+1
    return cos
    
def RazaoAurea(x,e):
    razao=2*(cos(x,e))
    return razao