# -*- coding: utf-8 -*-
from __future__ import division

#COMECE SEU CODIGO AQUI

investimentoInicial = input (' Digite o valor do investimento inicial: ')
taxaAnual= input (' Digite o valor da taxa anual: ')

x = taxaAnual/100.0

A1 = taxaInicial + (x*taxaInicial)
A2 = taxaInicial + (x*A1)
A3 = taxaInicial + (x*A2)
A4 = taxaInicial + (x*A3)
A5 = taxaInicial + (x*A4)
A6 = taxaInicial + (x*A5)
A7 = taxaInicial + (x*A6)
A8 = taxaInicial + (x*A7)
A9 = taxaInicial + (x*A8)
A10 = taxaInicial + (x*A9)

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
