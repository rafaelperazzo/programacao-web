# -*- coding: utf-8 -*-
peso=float(input('digite o peso:'))
altura=float(input('digite o a altura:'))
imc=peso/altura**2

if imc>0:
    imc<20:
        print('ABAIXO')
    20<imc>=25:
        print('NORMAL')
    25<imc>=30:
        print('SOBREPESO')
    30<imc>=40:
        print('OBESIDADEL')
    imc>40:
        print('OBESIDADE GRAVE')




