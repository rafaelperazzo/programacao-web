# -*- coding: utf-8 -*-
from __future__ import division
salas=input('Digite a quantidade de salas:')

a=[]
for i in range(0,salas,1):
    a.append(input('Digite uma quantidade de vidas para a sala:'))

entrada=input('Digite a porta de entrada:')
saida=input('Digite a porta de saída:')

vidas=0
for i in range(entrada,saida+1,1):
    vidas = vidas + a[i]

print vidas