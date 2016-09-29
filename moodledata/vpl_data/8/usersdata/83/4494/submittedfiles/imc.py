# -*- coding: utf-8 -*-
from __future__ import division

peso=input('Digite o peso em quilos: ')
altura=input('Digite a altura em metros: ')

imc=(peso/(altura)**2)
if imc<20:
    print ('Abaixo do peso')
elif 20<=imc<=25:
    print ('Peso Normal')
elif 25<imc<=30:
    print ('Sobrepeso')
elif 30<imc<=40:
    print ('Obesidade')
elif imc>40:
    print ('Obesidade grave')
