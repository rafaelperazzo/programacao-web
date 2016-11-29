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
        if 1<=m<=2000: #para m maior ou igual a 1 e menor ou igual a 2000
            if i%2==0: #se i for par
                expr = expr - (4/(x*(x+1)*(x+2)))

#caso contrário
            else:
                expr = expr + (4/(x*(x+1)*(x+2)))
        x = x +2
        i = i +1
#o valor de pi é igual a 3 + a expressão final
    calcula_pi = 3 + expr

#retorna o valor de pi
    return calcula_pi 

def fatorial(n):
    fatorial = 1
    for i in range (0, n, 1):
        fatorial = fatorial * i
    return fatorial
    
def calcula_co_seno(z, epsilon):
    soma = 0
    i = 1
    expoente = 2
    fracao = (z**expoente)/fatorial(expoente)
    while fracao>epsilon:
        fracao = (z**expoente)/fatorial(expoente)
        if i%2==1:
            soma = soma - fracao
        else:
            soma = soma + fracao
        expoente = expoente + 2
        i = i + 1
    calcula_co_seno = soma + 1
    return calcula_co_seno

def calcula_razao_aurea(m, epsilon):
    fi = 2 * (calcula_co_seno(calcula_pi(m)/5, epsilon))
    return fi
