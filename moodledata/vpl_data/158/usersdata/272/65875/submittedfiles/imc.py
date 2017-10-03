# -*- coding: utf-8 -*-

peso= float(input('Digite o peso:'))
altura= float(input('Digite a altura:'))

IMC=(peso/(altura**2))

if (IMC<20):
    print('ABAIXO')

elif (IMC>=20) and (IMC<=25):
    print('NORMAL')

elif (IMC>25) and (IMC<=30):
    print('SOBREPESO')

elif (IMC>30) and (IMC<=40):
    print('OBESIDADE')
    
elif (IMC>40):
    print('OBESIDADE GRAVE')