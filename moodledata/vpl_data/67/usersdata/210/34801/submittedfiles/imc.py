# -*- coding: utf-8 -*-
P=float(input('O VALOR DE SEU PESO:'))
H=float(input('O VALOR DE SUA ALTURA:'))
imc=P/H**2
if imc<20:
    print('ABAIXO')
elif 20<=imc<=25:
    print('NORMAL')
elif 25<imc<=30:
    print('SOBREPESO')
elif 30<imc<=40:
    print('OBESIDADE:')
elif imc>40:
    print('OBESIDADE GRAVE:')










