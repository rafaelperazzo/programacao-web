# -*- coding: utf-8 -*-
massa=float(input('digite a massa :'))
altura=float(input('digite a altura :'))
imc=massa/altura**2
if 20<=imc or imc<=25:
    print('normal')
if 25<imc or imc<=30:
    print('sobrepeso')
if 30<imc or imc<=40:
    print('obesidade')
if imc>40:
    print('obesidade grave')

