# -*- coding: utf-8 -*-

peso=float(input('Digite o peso:'))
altura=float(input('Digite a altura:'))

IMC=peso/(altura**2)

if IMC<20:
    print('ABAIXO')
if 20<=IMC and IMC<=25:
    print('NORMAL')
if 25<IMC and IMC<=30:
    print('SOBREPESO')
if 30<IMC and IMC<=40:
    print('OBESIDADE')
if IMC>40:
    print('OBESIDADE GRAVE')
