# -*- coding: utf-8 -*-
peso=float(input('Peso: '))
altura=float(input('altura: '))
imc=(peso)/(altura**2)
if imc<20:
    print('ABAIXO')
elif 20<=imc and imc<=25:
    print('NORMAL')
elif 25<imc and imc<=30:
    print('SOBREPESO')
elif 30<imc or imc<=40: 
    print('OBESIDADE')
else:
    print('OBESIDADE GRAVE')

