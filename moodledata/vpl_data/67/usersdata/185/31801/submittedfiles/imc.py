# -*- coding: utf-8 -*-
peso=float(input('digite o peso:'))
altura=float(input('digite a altura:'))
IMC=(peso)/(altura*altura)
if IMC<20:
    print('baixo')
if IMC<=25:
    print('normal')
if 25<IMC<=30:
    print('sobrepeso')
if 30<IMC<=40:
    print('obesidade')
if IMC>40:
    print('obesidade grave')