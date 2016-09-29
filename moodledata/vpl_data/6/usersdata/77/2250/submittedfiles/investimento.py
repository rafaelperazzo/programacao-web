# -*- coding: utf-8 -*-
from __future__ import division

investimentoInicial=input('Digite o valor do investimento inicial:')
taxaDeCrescimento=input('Digite o valor da taxa de crescimento percentual:')

investimento=investimentoInicial+taxaDeCrescimento*(investimentoInicial)

print('O valor do investimento será=%.2f:' %investimento)



