# -*- coding: utf-8 -*-

#COMECE AQUI ABAIXO

def hello_world() :
    print('Olá mundo')
    return

def hello_world2() :
    texto = 'Olá mundo'
    return texto

def media(n1,n2) :
    m = (n1 + n2)/2.0
    return m
    
def multiplicacao(x,y) :
    m = (x*y)
    return m

def media(n1,n2) :
    m = (n1 + n2)/2.0
    return m
    
def fatorial(n) :
    f = 1
    for i in range (2, n+1, 1):
        f *= i
    return f