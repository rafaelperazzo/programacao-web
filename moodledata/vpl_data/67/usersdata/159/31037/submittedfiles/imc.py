# -*- coding: utf-8 -*-
peso=float(input('Digite seu peso:'))
altura=float(input('Digite sua altura:'))
imc=(peso/(altura**2))
if imc<20:
    print('Abaixo do peso ideal')
elif imc>=20 and imc<=25:
    print('Peso normal')
elif imc>25 and imc<=30:
    print('Sobrepeso')
elif imc>30 and imc<=40:
    print('Obesidade')
elif imc>40:
    print('Obesidade grave')

