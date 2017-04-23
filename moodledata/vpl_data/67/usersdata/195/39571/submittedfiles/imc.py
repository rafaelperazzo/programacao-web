# -*- coding: utf-8 -*-
peso=float(input('digite o peso em kilos:'))
altura=float(input('digite a altura em metros:'))
imc=peso/altura*altura
if imc<20:
    print('abaixo')
elif imc>20 and imc<=25:
    print('normal')
elif imc>25 and imc<=30:
    print('sobrepeso')
elif imc>30 and imc<=40:
    print('obesidade')
elif imc>40:
    print('obesidade grave')

