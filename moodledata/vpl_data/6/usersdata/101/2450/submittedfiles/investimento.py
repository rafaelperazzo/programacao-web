# -*- coding: utf-8 -*-
from __future__ import division

#COMECE SEU CODIGO AQUI

investimentoInicial = input (' Digite o valor do investimento inicial: ')
taxaAnual= input (' Digite o valor da taxa anual: ')

x = taxaAnual/100.0

A1 = investimentoInicial + (x*investimentoInicial)
A2 = investimentoInicial + (x*A1)
A3 = investimentoInicial + (x*A2)
A4 = investimentoInicial + (x*A3)
A5 = investimentoInicial + (x*A4)
A6 = investimentoInicial + (x*A5)
A7 = investimentoInicial + (x*A6)
A8 = investimentoInicial + (x*A7)
A9 = investimentoInicial + (x*A8)
A10 = investimentoInicial + (x*A9)

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
