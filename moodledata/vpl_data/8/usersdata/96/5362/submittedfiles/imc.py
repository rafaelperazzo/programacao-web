# -*- coding: utf-8 -*-
from __future__ import division

Peso = input('Dgite o peso:')
Altura = input('Digite a altura:')

IMC = Peso/(Altura**2)
if IMC < 20:
    print('ABAIXO')
elif 20 <= IMC <= 25:
    print('NORMAL')
elif 25 < IMC <= 30:
    print('SOBREPESO')
elif 30 < IMC <= 40:
    print('OBESIDADE')
else:
    print('OBESIDADE GRAVE')
