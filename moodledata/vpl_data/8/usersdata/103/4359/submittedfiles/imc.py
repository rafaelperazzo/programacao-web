# -*- coding: utf-8 -*-
from __future__ import division
h=input('Insira a altura em metros:')
p=input('Insira o peso:')
Imc=p/(h**2)
if Imc<20:
    print('Abaixo')
if Imc>=20 and Imc<=25:
    print('Normal')
if Imc>25 and Imc<=30:
    print('Sobrepeso')
if Imc>30 and Imc<=40:
    print('Obesidade')
if Imc>40:
    print('Obesidade Grave')
