#ARQUIVO COM SUAS FUNCOES
from __future__ import division

def fatorial (x):
    som_fatorial=1
    for i in range (2,x+1,1):
        som_fatorial = som_fatorial * i
    return som_fatorial    
    
def calcula_valor_absoluto (m):
    if m < 0:
        m = m * (-1)
    return m
    
def calcula_pi (m):
    soma=0
    j=2
    calcula_valor_absoluto (m)
    for i in range (0,m,1):
        if i%2 ==0:
            soma = soma + (4 / (j * (j+1) * (j+2)) )
        else:
            soma = soma - (4 / (j * (j+1) * (j+2)) )
        j= j + 2
    soma_pi = 3 + soma     
    return soma_pi
    
def calcula_co_seno (z,e):
    i=1
    soma=0
    j=2
    a = (z**j) / fatorial (j)
    while a > e:
         a = (z**j) / fatorial (j)
         if i%2 !=0:
             soma = soma - a
         else:
             soma = soma + a
         j = j + 2
         i = i + 1
    cosseno = 1 - soma
    return cosseno

def calcula_razao_aurea (m,e):
    calcula_valor_absoluto (m)
    pi = calcula_pi (m)
    cosseno = calcula_co_seno (pi/5,e)
    razao_aurea = 2 * cosseno
    return razao_aurea
        
    
            