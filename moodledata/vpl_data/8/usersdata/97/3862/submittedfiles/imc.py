# -*- coding: utf-8 -*-
from __future__ import division

p=input('Digite o peso em quilos:')
h=input('Digite a altura em metros:')

imc=(p)/(h**2)

if imc<20:
    print('abaixo do peso')
elif 20<=imc<=25:
    print('peso normal')
elif 25<imc<=30:
    print('sobrepeso')
elif 30<imc<=40:
    print('obesidade')
elif imc>40:
    print('obesidade grave')




