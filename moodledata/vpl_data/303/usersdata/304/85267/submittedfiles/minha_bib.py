# -*- coding: utf-8 -*-
import time
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
        print ('Estou em %d' %i)
    return f
    
def cronometro(s) :
    for i in range (s,-1,-1):
        print('Faltam %d segundos' %i)
        time.sleep(1)
    print('ACABOOU')

def ler_inteiro() :
    m = int(input('Digite um inteiro: '))
    return m
    
def ler_inteiro_msg(mensagem) :
    m = int(input(mensagem))
    return m
    
def ler_float(mensagem) :
    m = float(input(mensagem))
    return m
    
def ler_baralho() :
    while(True) :
        carta = ler_inteiro()
        if (carta >= 1 and carta <= 13):
            break
        else:
            print('INVALIDA!')
    return carta