# -*- coding: utf-8 -*-
peso=float(input('digite peso:'))
altura=float(input('digite altura:'))
imc=peso/altura*altura
if imc<20:
    print('ABAIXO')
elif 20<=imc<=25:
    print('NORMAL')
elif 25<imc<=30:
    print('SOBREPESO')
elif 30<imc<=40:
    print('OBESIDADE')
else:
    if imc>40:
        print('OBESIDADE GRAVE')