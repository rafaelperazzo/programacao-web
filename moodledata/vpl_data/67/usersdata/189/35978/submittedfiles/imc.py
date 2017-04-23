# -*- coding: utf-8 -*-
peso=float(input('digite o peso:'))
altura=float(input('digite o a altura:'))
imc=peso/altura**2

if imc>0:
    imc<20
    20<imc>=25
    25<imc>=30
    30<imc>=40
    imc>40
print('ABAIXO')
print('NORMAL')
print('SOBREPESO')
print('OBESIDADEL')
print('OBESIDADE GRAVE')