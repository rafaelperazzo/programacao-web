# -*- coding: utf-8 -*-

peso=float(input('digite o peso em kg:'))
altura=float(imput('digite a altura em metros:'))
IMC=(peso)/(altura*altura)
if IMC<20:
    print('abaixo')
if 20<=IMC<=25:
    print('normal')
if 25<IMC<=30:
    print('sobrepeso')
if 30<IMC<=40:
    print('obesidade')
if IMC>40:
    print('obesiddegrave')