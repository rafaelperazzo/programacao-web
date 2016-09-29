# -*- coding: utf-8 -*-
from __future__ import division

peso=input('Digite o valor de seu peso em quilogramas:')
altura=input('Digite o valor da sua altura em metros:')


imc=(peso/(altura**2))

if imc<20:
    print('ABAIXO')
elif 20<=imc<=25:
    print('NORMAL')
elif 25<imc<=30:
    print('SOBREPESO')
elif 30<imc<=40:
    print('OBESIDADE')
elif imc>40:
    print('OBESIDADE GRAVE')