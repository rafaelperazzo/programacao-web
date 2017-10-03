# -*- coding: utf-8 -*-
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso/(altura**2)
if imc < 20:
    print('Baixo')
if imc <= 25 and imc >= 20:
    print('Normal')




