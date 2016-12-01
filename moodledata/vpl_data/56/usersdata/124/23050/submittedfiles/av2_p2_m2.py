# -*- coding: utf-8 -*-
from __future__ import division

def jogo(l, a, b):
    s = 0
    if b > a:
        for i in range (a,b+1,1):
            s = s + l[i]
    elif a >= b:
        for i in range (b,a+1,1):
            s = s + l[i]
    return s

n = input('Digite o número de salas: ')
l = []
for i in range (0,n,1):
    l.append(input('Digite um valor para a lista: '))
a = input('Digite a posição de entrada: ')
b = input('Digite a posição de saída: ')

print jogo(l, a, b)