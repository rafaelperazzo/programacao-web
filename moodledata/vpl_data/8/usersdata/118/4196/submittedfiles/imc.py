# -*- coding: utf-8 -*-
from __future__ import division

#1
p = input('Digite o valor do peso em kg :')
h = input('Digite o valor da altura em metros :')
#2
IMC = p/(h**2)

#3
if IMC<20 :
    print('ABAIXO')
if 20<=IMC<=25:
    print('NORMAL')
if 25<IMC<=30:
    print('SOBREPESO')
if 30<IMC<=40:
    print('OBESIDADE')
if IMC>40:
    print('OBESIDADE GRAVE')
