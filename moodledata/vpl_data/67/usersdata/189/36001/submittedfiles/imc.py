# -*- coding: utf-8 -*-
p=float(input('digite o peso:'))
a=float(input('digite o a altura:'))
imc=p/(a**2)
if imc<20:
    print('ABAIXO')
if 20<imc<=25:
    print('NORMAL')
if 25>imc<=30:
    print('SOBREPESO')
