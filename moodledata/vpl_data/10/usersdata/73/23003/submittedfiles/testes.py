# -*- coding: utf-8 -*-
from __future__ import division


qs=input('quantidade de salas:')

for i in range (0,qs,1):
    sala=[]
    sala.append(input('quantidade de vidas da sala:'))
print sala

pe=input('porta de entrada:')
ps=input('porta de saída:')
    

soma=0
for i in range(sala[pe],sala[ps]+1,1):
    a=sala[pe+i]
    soma=soma+a
    if sala[pe]==sala[ps]:
        break
print s