# -*- coding: utf-8 -*-
from __future__ import division

p=('Digite o peso em kilogramas:')
a=('Digite a altura em metros:')

imc=(p/(a**2))

if imc<20:
    print('ABAIXO')
if imc>=20 and imc<=25:
    print('NORMAL')
if imc>25 and imc<=30:
    print('SOBREPESO')
if imc>30 and imc<=40:
    print('OBESIDADE')
if imc>40:
    print('OBESIDADE GRAVE')