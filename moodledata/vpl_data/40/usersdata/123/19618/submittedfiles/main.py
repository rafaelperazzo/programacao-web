# -*- coding: utf-8 -*-
from __future__ import division
import funcoes

#ENTRADA
m= input('Insira a quantidade de termos da fórmula de pi:')
while m<1 or m>2000:
    m= input('Insira a quantidade de termos da fórmula de pi:')
e= input('Insira o valor de epsilon:')
while e<0 or e>1:
    e= input('Insira o valor de epsilon:')
#CHAMANDO FUNÇÕES PARA PROCESSAMENTO
u=(funcoes.pi(m)/5)
c=(funcoes.cos(u,e))
razaoaurea=2*c
#SAÍDA
print funcoes.pi(m)
print (razaoaurea)