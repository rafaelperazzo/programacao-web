#ARQUIVO COM SUAS FUNCOES
from __future__ import division

def calcula_valor_absoluto(x):
    if x < 0:
        return x*(-1)
    else:
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
    cont = 0
    resultado = 0
    multiplicacao = 1
    while cont<epsilon:
        cont = cont + 1
        if cont%2==0:
            multiplicacao = 1
        else:
            multiplicacao = -1
    resultado = z**calcula_valor_absoluto(cont)/fatorial(calcula_valor_absoluto(cont))*multiplicacao
    return resultado

def calcula_razao_aurea(m, epsilon):
    fi = 2 * calcula_co_seno(calcula_pi(m)/5, epsilon)
    return fi
