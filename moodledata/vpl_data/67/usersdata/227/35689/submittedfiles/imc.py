# -*- coding: utf-8 -*-
a=float(input('digite a altura:'))
p=float(input('digite o peso:'))

imc=p/(a**2)

if imc<20:
    print('%.1f'%'abaixo')
if 20<imc<=25:
    print('%.1f'%'normal')
if 25<imc<=30 :
    print('%.1f'%'sobre peso')
if 30<imc<=40:
    print('%.1f'%'obesidade')
else:
    print('%.1f'%'obesidade grave')



