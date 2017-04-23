# -*- coding: utf-8 -*-
peso=float(input('digite o peso em kilos:'))
altura=float(input('digite a altura em metros:'))
imc=peso/altura*altura
if imc<20:
    print('ABAIXO')
elif imc>=20 and imc<=25:
    print('NORMAL')
elif imc>25 and imc<=30:
    print('SOBREPESO')
elif imc>30 and imc<=40:
    print('OBESIDADE')
elif imc>40:
    print('OBESIDADE GRAVE')

