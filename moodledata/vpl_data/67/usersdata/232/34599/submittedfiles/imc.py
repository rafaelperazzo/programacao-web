# -*- coding: utf-8 -*-
Peso=float(input('Insira o peso: '))
Altura=float(input('Insira a Altura: '))
imc=(Peso/(Altura**2))
if imc<20:
    print('ABAIXO')
if 20<=imc<=25:
    print('NORMAL')
if 25<imc<=30:
    print('SOBREPESO')
if 30<imc<=40:
    print('OBESIDADE')
if imc>40:
    print('OBESIDADE GRAVE')

