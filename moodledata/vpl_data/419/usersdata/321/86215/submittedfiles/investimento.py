# -*- coding: utf-8 -*-
from __future__ import division

#COMECE SEU CODIGO AQUI
#Entrada
inv= float(input('Investimento anual: '))
cs= float(input('Taxa de crescimento anual: '))

#processamento

a= inv + (inv * cs)

x= 1

while (x < 11) :
    print('%.2f' % a)
    a= a + (a * cs)
    x= x + 1