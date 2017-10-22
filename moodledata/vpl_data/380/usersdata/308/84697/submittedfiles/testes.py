# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
def escrever(texto):
    print(texto)
def receberreal(texto):
    a = float(input(texto))
    return a
def soma(c, d):
    resultado = (c+d)
    return resultado
#####################################################
escreva('Olá mundo')
a = receberreal('Digite A: ')
b = receberreal('Digite B: ')
escrever(soma(a, b))

    
