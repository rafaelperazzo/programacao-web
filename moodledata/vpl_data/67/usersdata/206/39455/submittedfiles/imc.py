# -*- coding: utf-8 -*-
peso= float(input('Digite o peso:'))
altura= float(input('Digite a altura:'))

imc=peso/(altura*altura)

if imc<20:
    print('ABAIXO')
if imc>=20 and imc<=25:
    print('NORMAL')
if imc>25 and imc<=30:
    print('SOBREPESO')
if imc>30 and imc<=40:
    print('OBESIDADE')
if imc>40:
    print('OBESIDADE GRAVE')