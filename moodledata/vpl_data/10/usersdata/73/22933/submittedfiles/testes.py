# -*- coding: utf-8 -*-
from __future__ import division

qs=input('quantidade de salas:')

for i in range (0,qs,1):
    sala=[]
    sala.append(input('quantidade de vidas da sala:'))

pe=input('porta de entrada:')
ps=input('porta de saída:')

s=0
for j in range(sala[pe],sala[ps]+1,1):
    a=sala[pe]+sala[pe+j]
    s=s+a
    if sala[pe]==sala[ps]:
        break
print s