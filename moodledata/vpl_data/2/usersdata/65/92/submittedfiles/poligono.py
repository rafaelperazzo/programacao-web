# -*- coding: utf-8 -*-
from __future__ import division

#ENTRADA
n=input('Digite a quantidade de lados do polígono:')

#PROCESSAMENTO
nd=(n*(n-3.0)/float(2.0))

#SAIDA
print('Esse polígono tem %.1f diagonais diferentes' % nd)