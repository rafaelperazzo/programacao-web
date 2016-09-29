# -*- coding: utf-8 -*-
from __future__ import division

#COMECE SEU CODIGO AQUI

investimentoInicial = input (' Digite o valor do investimento inicial: ')
taxaAnual= input (' Digite o valor da taxa anual: ')

x = taxaAnual/100.0

A1 = investimentoInicial + (x*investimentoInicial)
A2 = investimentoInicial + (2*x*A1)
A3 = investimentoInicial + (3*x*A2)
A4 = investimentoInicial + (4*x*A3)
A5 = investimentoInicial + (5*x*A4)
A6 = investimentoInicial + (6*x*A5)
A7 = investimentoInicial + (7*x*A6)
A8 = investimentoInicial + (8*x*A7)
A9 = investimentoInicial + (9*x*A8)
A10 = investimentoInicial + (10*x*A9)

print ('%.2f' %A1)
print ('%.2f' %A2)
print ('%.2f' %A3)
print ('%.2f' %A4)
print ('%.2f' %A5)
print ('%.2f' %A6)
print ('%.2f' %A7)
print ('%.2f' %A8)
print ('%.2f' %A9)
print ('%.2f' %A10)
