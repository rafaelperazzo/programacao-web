# -*- coding: utf-8 -*-
from __future__ import division

peso = input (' digite o peso em kg: ')
altura = input (' digite a altura em m: ')

imc = peso  (altura)**2

if imc < 20:
    print ('BAIXO')
if 20 <= imc <= 25:
    print ('NORMAL')
if 25 < imc <= 30:
    print ('SOBREPESO')
if 30 < imc <= 40:
    print ('OBESIDADE')
if imc > 40:
    print('OBESIDADE GRAVE')