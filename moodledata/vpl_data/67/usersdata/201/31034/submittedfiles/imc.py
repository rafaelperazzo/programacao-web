# -*- coding: utf-8 -*-
Kg=float(input('Digite o peso:'))
h=float(input('Digite a altura:'))
IMC=(Kg/(h**2))
if IMC<20:
    print('Baixo')
if 20<IMC<=25:
    print('Normal')
if 25<IMC<=30:
    print('Sobrepeso')
if 30<IMC<=40:
    print('Obesidade')
if IMC>40:
    print('Obesidade Grave')


