# -*- coding: utf-8 -*-
peso=float(input('Digite seu peso em kg:'))
altura=float(input('Digite sua altura em metros:'))
IMC=peso/altura**2
if IMC<20:
    print('Baixo')
elif 20<=IMC<=25:
    print('Normal')
elif 25<IMC<=30:
    print('Sobrepeso')
elif 30<IMC<=40:
    print('Obesidade')
else:
    print('Obesidade grave')
