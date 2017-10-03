# -*- coding: utf-8 -*-
peso = float(input('Digite seu peso, em quilogramas: '))
altura = float(input('Digite sua altura, em metros: '))

imc = float(peso/(altura**2))

if imc < 20:
    print('ABAIXO')
elif (imc>20) and imc