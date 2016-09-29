# -*- coding: utf-8 -*-
from __future__ import division

peso=input('Digite seu peso:')
altura=input('Digite sua altura em metros')

imc=(peso)/((altura)**2)

if imc<20:
    print('abaixo')
    
elif 20<=imc<=25:
    print('normal')
    
elif 25<imc<=30:
    print('sobrepeso')
    
elif 30<imc<=40:
    print('obesidade')
    
elif imc>40:
    print('obesidade grave')