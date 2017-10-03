# -*- coding: utf-8 -*-
peso=float(input('Peso: '))
altura=float(input('altura: '))
imc=(peso)/(altura**2)
if imc<20:
    print('IMC<20-ABAIXO')
elif 20<=imc or imc<=25:
    print('20<=IMC<=25-NORMAL')
elif 25<imc or imc<=30:
    print('25<IMC<=30-SOBREPESO')
elif 30<imc or imc<=40: 
    print('30<IMC<=40-OBESIDADE')
else:
    print('IMC>40-OBESIDADE GRAVE')

