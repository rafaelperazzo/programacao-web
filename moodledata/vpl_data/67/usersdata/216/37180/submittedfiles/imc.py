# -*- coding: utf-8 -*-
peso= float(input('Digite o peso:'))
altura= float(input('Digite a altura:'))

imc=(peso)/(altura)**2

if imc<20:
    print('Abaixo')
elif 20<=imc and imc<=25:
    print('Normal')
elif 25<imc and imc<=30:
    print('Sobrepeso')
elif 30<imc and imc<=40:
    print('Obesidade')
else:
    print('Obesidade Grave')