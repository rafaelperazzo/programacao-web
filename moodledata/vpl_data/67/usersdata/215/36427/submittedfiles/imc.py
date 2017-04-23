# -*- coding: utf-8 -*-
p=float(input( 'digite o peso:'))
a=float(input( 'digite a altura:'))
imc=p/(a*a)
if imc<20:
    print('ABAIXO')
if imc>=20 and imc<=25:
    print ('NORMAL')
if imc>25 and imc<=30:
    print ('SOBRE PESO')
if imc>30 and imc<=40:
    print ('OBESIDADE')
if >40:
    print ('OBESIDADE GRAVE')
    