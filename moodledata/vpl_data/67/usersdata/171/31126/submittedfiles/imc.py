# -*- coding: utf-8 -*-
peso=float(input('digite o seu peso:'))
altura=float(input('digite a sua altura:'))
IMC=peso/(altura)**2
if IMC<20:
    print('ABAIXO')
elif 20<=IMC<=25:
    print('NORMAL')
elif 25<=IMC<=30:
    print('SOBREPESO')
elif 30<=IMC<=35:
    print('OBESIDADE')
elif IMC>40
