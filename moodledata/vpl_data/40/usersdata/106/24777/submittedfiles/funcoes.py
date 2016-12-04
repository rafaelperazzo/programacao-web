#ARQUIVO COM SUAS FUNCOES
# -*- coding: utf-8 -*-
from __future__ import division

#Estabelecer a função valor_absoluto para comparar o valor do cosseno com o epislon
def valorabsoluto(x):
    if x>=0:
        valorabsoluto = x
    else:
        valorabsoluto = x*(-1)
    return valorabsoluto

#calculo do valor de pi
def calculapi(m):
    pi = 3.00
    a=2.00
    variavel =1
    i=1
    while i<= m:
        pi = pi + ((variavel*4)/(a*(a+1)*(a+2)))
        a = a+2
        variavel = variavel*(-1)
        i=i+1
    return pi

#Para calcular a função cosseno, é necessário definir a função fatorial para os denominadores
def fatorial(a):
    fatorial = 1
    while a>=1:
        fatorial = fatorial*a
        a = a-1
    return fatorial
    
#Iniciarei o cosseno com cosz=1 para facilitar os cálculos, já que é a parte fixa para o cálculo de todos os cossenos
#criei uma variável p para facilitar no fator de correção do sinal
def calculacosseno(x,epislon):
    cosz = 1
    p = 1
    while True:
        cosz = cosz+((((x**2)**p)/fatorial(2*p))*((-1)**p))
        if valorabsoluto ((((x**2)**p)/fatorial(2*p))*((-1)**p)) > epislon:
            p = p+1
        else:
            break
    return cosz
    
def razaoaurea(m,epislon):
    z = (calculapi(m)/5)
    RA = 2*calculacosseno(z,epislon)
    return RA
    
