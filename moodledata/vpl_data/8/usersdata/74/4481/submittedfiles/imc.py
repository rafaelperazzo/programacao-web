# -*- coding: utf-8 -*-
from __future__ import division

kg = input('Peso')
h = input('Altura')

imc = kg/h**2

if imc<20:
    print('ABAIXO')
elif 20<=imc<=25:
    print('NORMAL')
elif 25<=imc<=30:
    print('NORMAL')
elif 30<=imc<=40:
    print('NORMAL')
else
    print('OBESIDADE GRAVE')