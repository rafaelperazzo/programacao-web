# -*- coding: utf-8 -*-
p=float(input('Digite o valor do peso: '))
h=float(input('Digite o valor de altura: '))
i=p/(h*h)
if i<20:
    print('ABAIXO')
if 25>=i and i>=20:
    print('NORMAL')
if i>25 and 30>=i:
    print('SOBREPESO')
if i>30 and 40>=i:
    print('OBESIDADE')
if i>40: 
    print('OBESIDADE GRAVE')

