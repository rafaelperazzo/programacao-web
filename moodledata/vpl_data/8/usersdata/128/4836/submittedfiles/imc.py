# -*- coding: utf-8 -*-
from __future__ import division

p=input('Peso em kg: ')
h=input('Altura em m: ')

imc= p/(h**2)

if imc < 20:
    print ('Abaixo')

elif imc >= 20 and imc <= 25:
    print ('Normal')

elif imc > 25 and imc <= 30:
    print ('Sobrepeso')

elif imc > 30 and imc <= 40:
    print ('Obesidade')

elif imc > 40:
    print ('Obesidade grave')