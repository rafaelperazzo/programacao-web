# -*- coding: utf-8 -*-

p= float(input(' digite o peso em kilos:'))
a= float(input(' digite a altura em metros:'))

i=p/(a**2)

if i<20:
    print('BAIXO')
elif 20<=i<=25:
    print('NORMAL')
elif 25<i>+30:
    print ('SOBREPESO')
elif 30<i<=40:
    print ('OBESIDADE')
elif i>40:
    print ('OBESIDADE GRAVE')

