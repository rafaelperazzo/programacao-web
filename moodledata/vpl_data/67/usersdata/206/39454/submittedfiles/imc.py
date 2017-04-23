# -*- coding: utf-8 -*-
peso= float(input('Digite o peso:'))
altura= float(input('Digite a altura:'))

imc=peso/(altura*altura)

if imc<20:
    print('Abaixo')
if imc>=20 and imc<=25:
    print('Normal')
if imc>25 and imc<=30:
    print('Sobrepeso')
if imc>30 and imc<=40:
    print('Obesidade')
if imc>40:
    print('Obesidade')