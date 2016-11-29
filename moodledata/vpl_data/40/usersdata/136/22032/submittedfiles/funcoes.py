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
    base = 1
    for i in range (n, 0, -1):
        base = base * i
    return base

def calcula_co_seno(z, epsilon):
    fracao = (z**expoente)/(fatorial(expoente))
    soma = 0
    i = 1
    expoente = 2
    while fracao>epsilon:
        fracao = (z**expoente)/(fatorial(expoente))
        if i%2!=0:
            soma = soma - fracao
        else:
            soma = soma + fracao
        expoente = expoente + 2
        i = i + 1
    cosseno = 1 + soma
    return cosseno

def calcula_razao_aurea(m, epsilon):
    fi = 2 * calcula_co_seno(calcula_pi(m)/5, epsilon)
    return fi
