# -*- coding: utf-8 -*-
from __future__ import division

n=input('Insira a quantidade de salas: ')

salas=[]
for i in range (0,n,1):
    salas.append(input('Digite a quantidade de vidas: '))

inicio=input('Insira a porta de entrada: ')
fim=input('Insira a porta de saída: ')


soma=0

for i in range (inicio, fim+1, 1):
    soma=soma+salas[i]

print soma