# -*- coding: utf-8 -*-
p=float(input('Digite seu peso em Kg:'))
a=float(input('Digite sua altura em m:'))
imc=p/(a*a)
if imc<20:
    print('ABAIXO')
if 20<=imc<=25:
    print('SOBREPESO')
if 25<imc<=30:
    print('OBESIDADE')
if imc>40:
    print('OBESIDADE GRAVE')

