#ARQUIVO COM SUAS FUNCOES
from __future__ import division

def calcula_valor_absoluto(x):
    if x < 0:
        x = x*(-1)
        return x

def calcula_pi(m):
    expr = 0
    i = 1
    x = 2
    while i<=m:
        if 1<=m<=2000: 
            if i%2==0: 
                expr = expr - (4/(x*(x+1)*(x+2)))
            else:
                expr = expr + (4/(x*(x+1)*(x+2)))
        x = x +2
        i = i +1
    calcula_pi = 3 + expr
    return calcula_pi 

def fatorial(n):
    fatorial = 1
    i = 1
    while i<=1:
        fatorial = fatorial * i
        i = i +1
    return fatorial
    
def calcula_co_seno(z, epsilon):
    soma = 0
    i = 1
    expoente = 2
    fracao = (z**expoente)/(fatorial(expoente))
    while fracao>epsilon:
        fracao = (z**expoente)/(fatorial(expoente))
        if i%2!=0:
            soma = soma - fracao
        else:
            soma = soma + fracao
        expoente = expoente + 2
        i = i + 1
    cosseno = soma + 1
    return cosseno

def calcula_razao_aurea(m, epsilon):
    fi = 2 * (calcula_co_seno(calcula_pi(m)/5, epsilon))
    return fi
