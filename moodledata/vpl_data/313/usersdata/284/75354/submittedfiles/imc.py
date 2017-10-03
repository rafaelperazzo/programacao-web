# -*- coding: utf-8 -*-
p=float(input('digite seu peso: '))
h=float(input('digite sua altura: '))
IMC=float(p/h**2)
if IMC<20:
    print('abaixo')
elif 20<=IMC<=25:
    print('normal')


