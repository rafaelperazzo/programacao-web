# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
def calcula_valor_absoluto(x):
    if x<0:
        x=x*(-1)
        return(x)
    else:
        return(x)

def calcula_pi(m):
    pi=3
    x=2
    for i in range(1,m+1,1):
        if i%2==0:
            pi=pi-((4)/(x*(x+1)*(x+2)))
        else:
            pi=pi-((4)/(x*(x+1)*(x+2)))
        x=x+2
    return(pi)

def calcula_fatorial(denominador2):
    i=1
    fatorial=1
    while i<=denominador2:
        fatorial=fatorial*i
        i=i+1
    return(fatorial)

def calcula_co_seno(z,epsilon):
    
