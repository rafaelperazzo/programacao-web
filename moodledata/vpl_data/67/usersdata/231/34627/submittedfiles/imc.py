# -*- coding: utf-8 -*-
massa=float(input('digite a massa :'))
altura=float(input('digite a altura :'))
imc=massa/(altura**2)
if 20<=imc or imc<=25:
    print('normal')
elif 25<imc or imc<=30:
    print('sobrepeso')
elif 30<imc or imc<=40:
    print('obesidade')
elif imc>40:
    print('obesidade grave')

