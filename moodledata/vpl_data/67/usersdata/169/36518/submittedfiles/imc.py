# -*- coding: utf-8 -*-
P=float(input('Digite o Peso em Kg:'))
H=float(input('Digite a Altura em Metros:'))
IMC=P/(H**2)
if (IMC<20):
   print('ABAIXO')
elif (20<=IMC<=25):
    print('NORMAL')
elif (25<IMC<=30):
    print('SOBREPESO')
elif (30<IMC<=40):
    print ('OBESIDADE')
else: 
    print('OBESIDADE GRAVE')
    