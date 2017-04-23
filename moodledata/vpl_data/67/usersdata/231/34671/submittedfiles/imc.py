# -*- coding: utf-8 -*-
m=float(input('digite a massa :'))
a=float(input('digite a altura :'))
imc=m/(a**2)
print('%.2f'%imc)
if imc<20:
    print('abaixo')
elif 20<=imc:
    print('normal')
elif imc<=25:
    print('normal')
elif 25<imc:
    print('sobrepeso')
