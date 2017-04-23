# -*- coding: utf-8 -*-
x1=(input('digite seu nome:')
p=float(input('Digite seu peso' + x1 + ':'))
h=float(input('Digite sua altura:'))
imc=p/h**2
if imc<20:
    print('abaixo')
elif 20<=imc<=25:
    print('normal')
elif 25<imc<=30:
    print('sobrepeso')
elif 30<imc<=40:
    print('obesidade')
elif imc>40:
    print('obesidade grave')

