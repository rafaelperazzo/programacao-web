# -*- coding: utf-8 -*-
from __future__ import division
h=input('Insira a altura em metros')
p=input('Insira o peso')
imc=p/(h**2)
if imc<20:
    print('Abaixo')
if imc>=20<=25:
    print('Normal')
if imc>=25<=30:
    print('Sobrepeso')
if imc>=30<=40:
    print('Obesidade')
if imc>40:
    print('Obesidade Grave')
