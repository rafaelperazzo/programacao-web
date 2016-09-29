# -*- coding: utf-8 -*-
from __future__ import division

#ENTRADA
vInicial = input('Digite o valor inicial do investimento:')
tPerc = input('Digite a taxa de crescimento percentual:')
tPercentual = tPerc/100

#PROCESSAMENTO
vAtualizado1 = vInicial + (tPercent * vInicial)
vAtualizado2 = vAtualizado1 + (tPercent * vAtualizado1)
vAtualizado3 = vAtualizado2 + (tPercent * vAtualizado2)
vAtualizado4 = vAtualizado3 + (tPercent * vAtualizado3)
vAtualizado5 = vAtualizado4 + (tPercent * vAtualizado4)
vAtualizado6 = vAtualizado5 + (tPercent * vAtualizado5)
vAtualizado7 = vAtualizado6 + (tPercent * vAtualizado6)
vAtualizado8 = vAtualizado7 + (tPercent * vAtualizado7)
vAtualizado9 = vAtualizado8 + (tPercent * vAtualizado8)
vAtualizado10 = vAtualizado9 + (tPercent * vAtualizado9)

#SAIDA
print('%.2f' %vAtualizado1)
print('%.2f' %vAtualizado2)
print('%.2f' %vAtualizado3)
print('%.2f' %vAtualizado4)
print('%.2f' %vAtualizado5)
print('%.2f' %vAtualizado6)
print('%.2f' %vAtualizado7)
print('%.2f' %vAtualizado8)
print('%.2f' %vAtualizado9)
print('%.2f' %vAtualizado10)
