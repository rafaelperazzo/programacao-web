# -*- coding: utf-8 -*-
from __future__ import division

peso = input('digite seu peso: ')
altura = input('digite sua altura: ')

imc = peso/altura**2
if 20<=imc<=25:
    print ('NORMAL')
else:
    25<imc<=30:
        print ('SOBREPESO')
else: 
    30<imc<=40:
        print ('OBESIDADE')
else:
    imc>40:
        print ('OBESIDADE GRAVE')