# -*- coding: utf-8 -*-
p=float(input('Diga seu peso em quilos:'))
a=float(input('Diga sua altura em metros:'))
imc=(p/(a**2))
if imc<20:
    print('ABAIXO')
elif 20<=imc<=25:
    print('NORMAL')
elif 25<imc<=30:
    print('SOBREPESO')
elif 30<imc<=40:
    print('OBESIDADE')
elif imc>40:
    print('OBESIDADE GRAVE')
    

