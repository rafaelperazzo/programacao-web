# -*- coding: utf-8 -*-
p=float(input('digite o peso:'))
h=float(input('digite o a altura:'))
IMC=p/(h**2)
if IMC<20:
    print('abaixo')
if 20<=IMC<=25:
    print('normal')
if 25<=IMC<=30:
    print('sobrepeso')
if 30<=IMC<=40:
    print('obesidade')
if IMC>40:
    print('obesidade grave')


