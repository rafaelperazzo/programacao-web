# -*- coding: utf-8 -*-
P=float(input('digite seu peso em kilos:'))
A=float(input('digite sua altura em metros:'))
imc= P/(A*A)
if imc<20:
    print('ABAIXO')
elif 20<=imc<=25:
    print('NORMAL')
else:
    if 25<imc<=30:
        print('SOBREPESO')
    elif 30<imc<=40:
        print('OBESIDADE')
    else:
        if imc>40:
            print('OBESIDADE GRAVE')

