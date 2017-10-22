# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO

p = float(input('Digite o p: '))
h = float(input('Digite o h: '))

imc  = p /(h**2)

if (imc<20):
    print ('abaixo')
if (20<=imc<=25):
    print ('normal')
if (25<imc<=30):
    print ('sobrepeso')
if (30<imc<=40):
    print ('obesidade')
if (imc>40):
    print('obesidade grave')