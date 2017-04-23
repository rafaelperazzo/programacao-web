# -*- coding: utf-8 -*-
m=float(input('digite a massa :'))
a=float(input('digite a altura :'))
imc=m/(a**2)
print('%.2f'%imc)
if imc<20:
    print('abaixo')
if 20<=imc:
    print('normal')
if imc<=25:
    print('normal')
if imc>25:
    print('sobrepeso')
