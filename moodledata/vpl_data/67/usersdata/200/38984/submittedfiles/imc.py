# -*- coding: utf-8 -*-
x=float(input('digite o valor do peso:'))
y=float(input('digite o valor da altura:'))
imc=x/(y**2)
if imc<20:
    print('ABAIXO')
if 20<=imc<=25:
    print('NORMAL')
if 25<imc<=30:
    print('SOBREPESO')
if 30<imc<=40:
    print('OBESIDADE')
if imc>40:
    print('OBESIDADE GRAVE')
