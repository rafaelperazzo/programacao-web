# -*- coding: utf-8 -*-
from __future__ import division

numSalas = input ('Digite o número de salas:')

p = []
soma = 0

for i in range (0,numSalas,1):
    p.append (input('Digite a quantidade de vidas:'))
    
entrada = input ('Digite a porta de entrada:')
saida = input ('Digite a porta de saída:')

if (entrada==saida):
    soma = soma + p[entrada]

elif (entrada < saida):
    i = entrada
    while (i <= saida):
        soma = soma + p[i]
        i = i +1
        
else:
    i = saida
    while (i < entrada):
        soma = soma + p[i]
        i = i +1
   
print (soma)
        
