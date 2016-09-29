# -*- coding: utf-8 -*-
from __future__ import division
p=input('Insira a altura em metros:')
h=input('Insira o peso:')
Imc=p/(h**2)
if Imc<20:
    print('ABAIXO')
if 20<=Imc<=25:
    print('NORMAL')
if 25<Imc<=30:
    print('SOBREPESO')
if 30<Imc<=40:
    print('OBESIDADE')
if Imc>40:
    print('OBESIDADE GRAVE')
