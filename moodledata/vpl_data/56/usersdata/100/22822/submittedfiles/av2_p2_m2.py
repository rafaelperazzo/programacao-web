# -*- coding: utf-8 -*-
from __future__ import division
qs =  input ('Quantidade de salas:')
#qv = input ('Quantidade de vidas:')
pe = input('Porta de entrada:')
ps = input('Porta de saída:')
for i in range(0,qs,1):
    sala = []
    sala.append(input ('Quantidade de vidas:'))
s = 0
for j in range(sala[pe],sala[pe]==sala[ps],1):
    a = sala[pe]+sala[pe+j]
    s = s+a
print s