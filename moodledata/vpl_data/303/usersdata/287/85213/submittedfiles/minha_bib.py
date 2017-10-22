# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
import time
def hello_word():
    print('ola mundo')
    return
    
def media(n1,n2):
    m=(n1+n2)/2.0
    return m

def multiplicacao(x,y):
    m=(x*y)
    return m

def fatorial(n):
    f=1
    for i in range(2,n+1,1):
        f*=i
        print('estou passando %d' %i)
    return f

def cronometro(s):
    for i in range(s,-1,-1):
        print('%d segundos' %i)
        time.sleep(1)
    print('acabouuuu!!')
    
def ler_inteiro():
    i=int(input('digite um inteiro: '))

