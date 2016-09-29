# -*- coding: utf-8 -*-
from __future__ import division

p=input('Digite o peso em quilos:')
a=input('Digite a altura em metros:')

imc = (p/(a**2))

if imc<20:
    print('ABAIXO')
elif imc>=20 and imc<=25:
    print('NORMAL')
elif imc>25 and imc<=30:
    print('SOBREPESO')
elif imc>30 and imc<=40:
    print('OBESIDADE')
elif imc>40:
    print('OBESIDADE GRAVE')