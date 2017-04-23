# -*- coding: utf-8 -*-
a=float(input('Digite o peso em kg: '))
b=float(input('Digite o a altura em metros: '))
imc=(a)/(b**2)
if  imc<20:
    print('ABAIXO')
if  20<=imc<=25:
    print('NORMAL')
