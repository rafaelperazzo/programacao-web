# -*- coding: utf-8 -*-
p=float(input('digite peso em kg: '))
a=float(input('digite altura em metros: '))

imc=p/(a*a)

if imc<20:
    print('abaixo')
if 20<imc<=25:
    print('normal')
if 25<imc<=30:
    print('sobrepeso')
if 30<imc<=40:
    print('obesidade')
if imc>40:
    print('obesidade grave')

