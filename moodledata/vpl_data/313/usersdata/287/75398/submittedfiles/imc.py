# -*- coding: utf-8 -*-
p=float(input('Digite seu peso em kg: '))
a=float(input('Digite sua altura em metros: '))
imc=((p)/(a**2))
if imc < 20:
    print('ABAIXO')
if imc>=20 and imc<=25:
    print('NORMAL')
if imc>25 and imc<=30:
    print('SOBREPESO')
if imc>30 and imc<=40:
    print('OBESIDADE')
if imc>40:
    print('OBESIDADE GRAVE')


