# -*- coding: utf-8 -*-
from __future__ import division
qs =  input ('Quantidade de salas:')
#qv = input ('Quantidade de vidas:')
pe = input('Porta de entrada:')
ps = input('Porta de saída:')
'''Faremos abaixo o código que dirá quantas vidas o jogador receberá se escolher
uma das portas no sentido crescente(esquerda para a direita).'''
sala=[]
for i in range(0,qs,1):
    sala.append(input ('Quantidade de vidas:'))
if pe<ps:
    s1=0
    for j in range(1,(ps-pe),1):
        a = sala[pe+j]
        s1 = s1+a
    tot = s1+sala[pe]+sala[ps]
    print tot
'''Abaixo será definido o código caso o jogador escolha portas no sentido
decrescente(direita para esquerda)'''
if pe>ps:
    s1=0
    for j in range(1,(pe-ps),1):
        a = sala[ps+j]
        s1 = s1+a
    tot = s1+sala[pe]+sala[ps]
    print tot