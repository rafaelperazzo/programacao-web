# -*- coding: utf-8 -*-
from __future__ import division

numSalas = input ('Digite o número de salas:')
entrada = input ('Digite a porta de entrada:')
saida = input ('Digite a porta de saída:')

p = []
soma = 0

for i in range (0,numSalas,1):
    p.append (input('Digite a quantidade de vidas:'))

if (entrada<=saida):
    while (entrada <= saida):
        soma = soma + p[i]
        entrada = entrada +1
        
else:
    while (saida <= entrada):
        soma = soma + p[i]
        saida = saida +1
   
print (soma)
        
