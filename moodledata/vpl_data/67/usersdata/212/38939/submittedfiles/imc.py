# -*- coding: utf-8 -*-
x=float(input('digite o peso:'))
y=float(input('digite a altura'))
imc=x/(y**2)
if imc<20:
    print('abaixo')
elif 20<=imc<=25:
    print('normal')
elif 25<=imc<=30:
    print('sobrepeso')
elif 30<=imc<=40:
    print('obesidade')
else:
    print('obesidade grave')
