# -*- coding: utf-8 -*-
from __future__ import division

#ENTRADA
vInicial = input('Digite o valor inicial do investimento:')
tPerc = input('Digite a taxa de crescimento percentual:')

#PROCESSAMENTO
vAtualizado1 = vInicial + (tPerc * vInicial)
vAtualizado2 = vAtualizado1 + (tPerc * vAtualizado1)
vAtualizado3 = vAtualizado2 + (tPerc * vAtualizado2)
vAtualizado4 = vAtualizado3 + (tPerc * vAtualizado3)
vAtualizado5 = vAtualizado4 + (tPerc * vAtualizado4)
vAtualizado6 = vAtualizado5 + (tPerc * vAtualizado5)
vAtualizado7 = vAtualizado6 + (tPerc * vAtualizado6)
vAtualizado8 = vAtualizado7 + (tPerc * vAtualizado7)
vAtualizado9 = vAtualizado8 + (tPerc * vAtualizado8)
vAtualizado10 = vAtualizado9 + (tPerc * vAtualizado9)

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
