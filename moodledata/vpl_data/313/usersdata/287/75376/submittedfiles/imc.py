# -*- coding: utf-8 -*-
p=int(input('Digite seu peso em kg: '))
a=int(input('Digite sua altura em metros: '))
imc=((p)/(a**2))
if imc < 20:
    print('NORMAL')
if imc>=20 and imc<=25:
    print('SOBREPESO')
if imc>25 and imc<=30:
    print('OBESIDADE')
if imc>40:
    print('OBESIDADE GRAVE')


