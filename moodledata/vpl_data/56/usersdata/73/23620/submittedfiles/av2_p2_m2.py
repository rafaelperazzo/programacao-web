# -*- coding: utf-8 -*-
from __future__ import division

qs=input('Quantidade de salas:')

sala=[]
for i in range (0,qs,1):
    sala.append(input('quantidade de vidas da sala:'))

pe=input('porta de entrada:')
ps=input('porta de saída:')

soma=0
i=0
if pe<ps:
    s1=0
    for j in range(1,(ps-pe),1):
        a=sala[pe+j]
        s1=s1+a
    tot=s1+sala[pe]+sala[ps]
    print tot
   
if pe>ps:
    s1=0
    for j in range(1,(pe-ps),1):
        a=sala[ps+j]
        s1=s1+a
    tot=s1+sala[pe]+sala[ps]
    print tot
   


