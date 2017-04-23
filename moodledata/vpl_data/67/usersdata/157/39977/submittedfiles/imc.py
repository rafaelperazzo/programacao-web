# -*- coding: utf-8 -*-
peso=float(input('Digite seu peso: '))
altura=float(input('Digite sua altura: '))
IMC=peso/(ltura**2)
if (IMC<20):
    print('abaixo')
elif (20<=IMC<=25):
    print('normal')
elif (25<IMC<=30):
    print('sobrepeso')
elif(30<IMC<=40):
    print('obesidade')
else:
    print('obesidade grave')

