# -*- coding: utf-8 -*-
from __future__ import division

numSalas = input ('Digite o número de salas:')

portas = []
for i in range (0,numSalas, 1):
    portas.append ('Digite a quantidade de vidas:')

entrada = input ('Digite a porta de entrada:')
saida = input ('Digite a porta de saída:')

soma=0

if (entrada==saida):
    soma = portas[entrada]

elif (entrada<saida):
    i=entrada
    while (i<=saida):
        soma = soma+portas[i]
        
else:
    i=saida
    while (i<=entrada):
        soma = soma+portas[i]
   
print (soma)
        
