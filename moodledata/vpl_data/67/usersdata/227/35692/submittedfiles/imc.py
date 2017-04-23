# -*- coding: utf-8 -*-
a=float(input('digite a altura:'))
p=float(input('digite o peso:'))

imc=p/a**2

if imc<20:
    print('abaixo')
if 20<imc<=25:
    print('normal')
if 25<imc<=30 :
    print('sobre peso')
if 30<imc<=40:
    print('obesidade')
if imc>40:
    print('obesidade grave')



