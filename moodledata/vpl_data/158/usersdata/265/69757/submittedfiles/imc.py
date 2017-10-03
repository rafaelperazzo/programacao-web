# -*- coding: utf-8 -*-
p = float(input('digite o valor do peso em quilogramas: '))
h = float(input('digite o valor da altura em metros: '))
imc = (p/(h**2))
if imc<20:
    print('baixo')
if 20<=imc<=25:
    print('normal')
if 25<imc<=30:
    print('sobrepeso')
if 30<imc<=40:
    print('obesidade')
if imc>40:
    print('obesidade grave')

