# -*- coding: utf-8 -*-
peso=float(input('digite o peso:'))
altura=float(input('digite o a altura:'))
imc=peso/altura**2

if imc<20:
        print('ABAIXO')
    elif 20<imc>=25:
        print('NORMAL')
    elif 25<imc>=30:
        print('SOBREPESO')
    elif 30<imc>=40:
        print('OBESIDADEL')
    elif imc>40:
        print('OBESIDADE GRAVE')




