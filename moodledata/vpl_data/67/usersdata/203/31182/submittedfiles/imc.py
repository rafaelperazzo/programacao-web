# -*- coding: utf-8 -*-
peso=float(input('Digite seu peso em kg: '))
altura=float(input('Digite sua altura em m: '))
IMC=(peso)/(altura**2)
if IMC<20:
    print('ABAIXO')
elif 20<=IMC and IMC<=25:
    print('NORMAL')
elif 25<IMC and IMC<=30:
    print('SOBREPESO')
elif 30<IMC and IMC<=40:
    print('OBESIDADE')
else:
    print('OBESIDADE GRAVE')