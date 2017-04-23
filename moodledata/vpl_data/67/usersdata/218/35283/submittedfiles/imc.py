# -*- coding: utf-8 -*-
peso=float(input('digite o valor do seu peso em kilos:'))
altura=float(input('digite a sua altura em metros:'))
IMC=peso/(altura*altura)
if IMC<20:
    print('abaixo')
if IMC>=20:
    if IMC<=25:
        print('NORMAL.')
if IMC>25:
    if IMC<=30:
        print('SOBREPESO.')
if IMC>30:
    if IMC<=40:
        print('OBESIDADE.')
elif:
    print('OBESIDADE GRAVE.')