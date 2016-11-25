# -*- coding: utf-8 -*-
from __future__ import division
import funcoes

m=int(input('Digite m:'))
epsilon=input('Digite o epsilon para o cosseno:')

def fatorial(n):
    n_fat=1
    for i in range(1,n+1,1):
        n_fat*=i
    return n_fat

def calcula_valor_absoluto(x):
    if x<0:
        x=x*(-1)
    return x

def pi(m):    
    soma=0
    j=2
    for i in range (1,m+1,1):
        if i%2==0:
            soma=soma-(4/(j*(j+1)*(j+2)))
        else:
            soma=soma+(4/(j*(j+1)*(j+2)))
        j=j+2    
    pi=3+soma
    return pi
    

print ('%.15f' %pi(m))

z=pi(m)
def calcula_co_seno(z,epsilon):
    parcela=1
    soma_cos=1
    a=2
    i=2
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

def calcula_razao_aurea(m,epsilon):
    razao= 2*(calcula_co_seno(pi(m)/5,epsilon))
    return razao

print ('%.15f' %calcula_razao_aurea(m,epsilon))