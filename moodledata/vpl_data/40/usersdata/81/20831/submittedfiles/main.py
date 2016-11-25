# -*- coding: utf-8 -*-
from __future__ import division
import funcoes

#Pedindo ao usúario o número de termos e o valor do epsilon
m=int(input('Digite o número m de termos da fórmula de pi:'))
epsilon=input('Digite o epsilon para o cálculo da razão aurea:')

#Calculando Fatorial
def fatorial(n):
    n_fat=1
    for i in range(1,n+1,1):
        n_fat*=i
    return n_fat

#Calculando Valor Absoluto
def calcula_valor_absoluto(x):
    if x<0:
        x=x*(-1)
    return x

#Calculando a fórmula de pi
def pi(m):    
    soma=0
    t=2
    for i in range (1,m+1,1):
        if i%2==0:
            soma=soma-(4/(t*(t+1)*(t+2)))
        else:
            soma=soma+(4/(t*(t+1)*(t+2)))
        t=t+2    
    pi=3+soma
    return pi
    
#Mostrando ao usúario o valor aproximado de pi
print ('Valor aproximado de pi: %.15f' %pi(m))


#Calculando o valor de cosseno
z=pi(m)
def calcula_co_seno(z,epsilon):
    parcela=1
    soma_cos=0
    a=2
    i=1
    while True:
        if parcela>=epsilon:
            if i%2!=0:
                soma_cos=soma_cos+parcela
            else:
                soma_cos=soma_cos-parcela
        if parcela<epsilon:
            break
        parcela=(calcula_valor_absoluto(((z)**a)/fatorial(a)))
        a=a+2
        i=i+1
    return soma_cos

#Calculando valor da razão aurea
def calcula_razao_aurea(m,epsilon):
    razao= 2*(calcula_co_seno(pi(m)/5,epsilon))
    return razao

#Mostrando ao usuário o valor aproximado da razão aurea
print ('Valor aproximado da razão aurea: %.15f' %calcula_razao_aurea(m,epsilon))