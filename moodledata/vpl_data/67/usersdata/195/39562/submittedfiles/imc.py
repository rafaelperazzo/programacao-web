# -*- coding: utf-8 -*-
peso=float(input('digite o peso em kilos:'))
altura=float(input('digite a altura em metros:'))
imc=peso/altura*altura
if imc<20:
    print('ABAIXO')
elif 20<=imc and imc<=25:
    print('NORMAL')
elif 25<imc and imc<=30:
    print('SOBREPESO')
elif 30<imc and imc<=40:
    print('OBESIDADE')
elif imc>40:
    print('OBESIDADE GRAVE')

