# -*- coding: utf-8 -*-
p= float(input('Digite seu peso: '))
a= float(input( 'Digite sua altura :'))
imc= p/a**2
if 20>imc:
    print('ABAIXO')
if 20<= imc <=25:
    print('NORMAL')
if 25<= imc >=30:
    print('SOBREPESO')
if 30<= imc <=40:
    print('OBESIDADE')
if 40< imc:
    print('OBESIDADE GRAVE')



