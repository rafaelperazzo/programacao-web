# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
def escrever(texto):
    print(texto)
def receberreal(texto):
    a = float(input(texto))
    return a
    
def multiplicacao(c, d):
    resultado = (c*d)
    return resultado
def soma(c, d):
    resultado = (c+d)
    return resultado
#####################################################
escrever('Olá mundo')
a = receberreal('Digite A: ')
b = receberreal('Digite B: ')
escrever(soma(a, b))
escrever(multiplicacao(a, b))

    
