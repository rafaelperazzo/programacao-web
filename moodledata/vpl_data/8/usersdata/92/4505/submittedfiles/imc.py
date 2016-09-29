# -*- coding: utf-8 -*-
from __future__ import division

p= input('Digite o valor do peso: ')
h= input('Digite o valor da altura: ')

imc= p/((h)**(2))

if imc < 20:
    print('ABAIXO')

if 20<=imc and imc<=25:
    print('NORMAL')

if 25<imc and imc<=30:
    print('SOBREPESO')

if 30<imc and imc<=40:
    print('OBESIDADE')

if imc>40:
    print('OBESIDADE GRAVE')