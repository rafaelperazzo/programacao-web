# -*- coding: utf-8 -*-
p= float(input('Digite seu peso: '))
a= float(input( 'Digite sua altura :'))
imc= p/a**2
if 20>imc:
    print('ABAIXO')
elif 20<= imc <=25:
    print('NORMAL')
elif 25<= imc >=30:
    print('SOBREPESO')
elif 30<= imc <=40:
    print('OBESIDADE')
elif 40< imc:
    print('OBESIDADE GRAVE')



