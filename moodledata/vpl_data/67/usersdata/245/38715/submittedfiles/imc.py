# -*- coding: utf-8 -*-
p=float(input('Digite seu peso em Kg:'))
a=float(input('Digite sua altura em m:'))
icm=p/(a**2)
if icm<20:
    print('ABAIXO')
elif 20<=icm<=25:
    print('NORMAL')
elif 25<icm<=30:
    print('SOBREPESO')
elif 30<icm<=40:
    print('OBESIDADE')
elif icm>40:
    print('OBESIDADE GRAVE')

