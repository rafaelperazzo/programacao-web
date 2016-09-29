# -*- coding: utf-8 -*-
from __future__ import division

valor = input('DIGITE O VALOR DO INVESTIMENTO INICIAL: ')
taxa = input('DIGITE A TAXA DE CRESCIMENTO PERCENTUAL: ')

a = valor+valor*taxa
b = a+valor*taxa

print a
print b