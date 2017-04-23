# -*- coding: utf-8 -*-
peso=float(input('digite o peso:'))
altura=float(input('digite a altura:'))
imc=peso/(altura*altura)
if imc<20:
    print('ABAIXO')
elif 20<=imc<=25:
    print('normal')
elif 25<=imc<=30:
    print('sobrepeso')
elif 30<=imc<=35:
    print('obesidade')
else:
    print('obesidade grave')

