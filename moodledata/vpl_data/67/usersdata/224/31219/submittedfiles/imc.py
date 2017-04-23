# -*- coding: utf-8 -*-
p=float(input('Digite o seu peso: '))
h=float(input('Digite a sua altura: '))
IMC=p/(h*h)
if IMC<20:
    print('Abaixo do peso')
if 20<=IMC<=25:
    print('Peso normal')
if 25<IMC<=30:
    print('Sobrepeso')
if 30<=IMC<=40:
    print('Obesidade')
if IMC>40:
    print('Obesidade grave')