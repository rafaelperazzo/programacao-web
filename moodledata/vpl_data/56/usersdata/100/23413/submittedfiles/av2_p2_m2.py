# -*- coding: utf-8 -*-
from __future__ import division
qs =  input ('Quantidade de salas:')
#qv = input ('Quantidade de vidas:')
pe = input('Porta de entrada:')
ps = input('Porta de saída:')
for i in range(0,qs,1):
    sala = []
    sala.append(input ('Quantidade de vidas:'))
if pe<ps:
    s1=0
    for i in range(1,(ps-pe),1):
        a = sala[pe+i]
        s1=s1+a
    tor = s1+sala[pe]+sala[ps]
    print tot
if pe>ps:
    s2=0
    for j in range(1,(pe-ps),1):
        a = sala[ps+j]
        s2=s2+a
    tot = s2+sala[pe]+sala[ps]
    print tot