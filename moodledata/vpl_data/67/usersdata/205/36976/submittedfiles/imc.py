# -*- coding: utf-8 -*-
peso=float(input('digite o peso em kilo:'))
altura=float(input('digite a altura em metros:'))
imc=(peso/(altura**2))

if(imc<20):
    print('abaixo')
if(20<=imc<=25):
    print('normal')
if (25<imc<=30):
    print('sobrepeso')
if(30<=imc<=40):
    print( ' obesidade')
if(imc>=40):
    print('obesidade grave')


