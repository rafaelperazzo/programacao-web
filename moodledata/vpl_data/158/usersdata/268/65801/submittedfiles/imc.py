# -*- coding: utf-8 -*-

p=float(input('Digite seu peso'))
a=float(input('Digite sua altura'))

IMC= p/(a**2)

if (IMC<20):
    print('ABAIXO')
elif (20<= IMC <=25):
    print('NORMAL')
elif (25< IMC <= 30):
    print('SOBREPESO')
elif (30< IMC <= 40):
    print('OBESIDADE')
elif (IMC > 40):
    print('OBESIDADE GRAVE')
