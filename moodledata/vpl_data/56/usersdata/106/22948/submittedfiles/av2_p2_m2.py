# -*- coding: utf-8 -*-
from __future__ import division

def soma (a,entrada,saida):
    Soma = 0
    for i in range (entrada, saida+1, 1):
        Soma= Soma +a[i]
        return Soma

n = input ('Digite a quantidade de salas:')
a= []
for i in range (0,n,1):
    a.append (input('Digite a quantidade de vidas:'))
entrada = input ('Digite a sala de entrada:')
saida = input ('Digite a sala de saída:')
print ( soma (a,entrada,saida))