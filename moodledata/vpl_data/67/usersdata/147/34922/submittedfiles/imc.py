# -*- coding: utf-8 -*-
peso=float(input('digite peso:'))
altura=float(input('digite altura:'))
imc=peso/altura
if imc<20:
    print('abaixo')
elif 20<=imc<=25:
    print('normal')
elif 25<imc<=30:
    print('sobrepeso')
elif 30<imc<=40:
    print('obesidade')
else imc>40:
    print('obesidade grave')

