# -*- coding: utf-8 -*-
from __future__ import division

#COMECE SEU CODIGO AQUI

investimentoInicial = input (' Digite o valor do investimento inicial: ')
taxaAnual= input (' Digite o valor da taxa anual: ')

A1 = investimentoInicial + (taxaAnual*investimentoInicial)
A2 = A1 + (taxaAnual*A1)
A3 = A2 + (taxaAnual*A2)
A4 = A3 + (taxaAnual*A3)
A5 = A4 + (taxaAnual*A4)
A6 = A5 + (taxaAnual*A5)
A7 = A6 + (taxaAnual*A6)
A8 = A7 + (taxaAnual*A7)
A9 = A8 + (taxaAnual*A8)
A10 = A9 + (taxaAnual*A9)

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