# -*- coding: utf-8 -*-
from __future__ import division
n=input('Digite a quantidade de salas: ')
sala=[]
for i in range(0,n,1):
    sala.append(input('Digite a quantidade de vida : '))
pe=input('Digite porta de entrada: ')
ps=input(' Digite porta de saida: ')
soma=0
for i in range(pe,ps+1,1):
    soma=soma+sala[i]
print(soma)
