# -*- coding: utf-8 -*-
from __future__ import division

a=input('Digite o seu peso: ')
b=input('Digite sua altura: ')

imc=a/(b**2)

if imc<20:
    print('ABAIXO')
if 20<=imc<=25:
    print('NORMAL')
if 25<imc<=30:
    print('SOBREPESO')
if 30<imc<=40:
    print('OBESIDADE')
if 40<imc:
    print('OBESIDADE GRAVE')