# -*- coding: utf-8 -*-
from __future__ import division

#Entrada
n = input('Digite o número de salas:')
l = []
for i in range(0,n,1):
    l.append(input('Digite a quantidade de vidas para a sala:'))
    
pe = input('Digite o número da porta de entrada:')
ps = input('Digite o número da porta de saída:')

#Processamento
soma = 0
for i in range(pe,ps+1,1):
    soma = soma + l[i]
    
#Saída
print(int(soma))
