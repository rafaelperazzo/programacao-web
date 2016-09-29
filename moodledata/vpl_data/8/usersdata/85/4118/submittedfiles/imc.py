# -*- coding: utf-8 -*-
from __future__ import division

p= input('Digite seu peso: ')
h= input('Digite sua altua: ')

imc= p/(h**2)

if imc<20:
    print('Abaixo do peso')
elif imc>=20 and imc>=25:
    print('Normal')
elif imc>25 and imc<=30:
    print('Sobrepeso')
elif imc> 20 and imc<=40:
    print('Obesidade')
else:
    print('Obessidade grave')