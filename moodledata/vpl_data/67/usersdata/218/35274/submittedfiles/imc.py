# -*- coding: utf-8 -*-
peso=float(input('digite o valor do seu peso:'))
altura=float(input('digite a sua altura:'))
IMC=peso/(altura*altura)
if IMC<20:
    print('abaixo')
elif IMC>=20:
    if IMC<=25:
        print('NORMAL.')
elif IMC>25:
    if IMC<=30:
        print('SOBREPESO.')
elif IMC>30:
    if IMC<=40:
        print('OBESIDADE.')
else:
    print('OBESIDADE GRAVE.')