# -*- coding: utf-8 -*-
from __future__ import division

Peso=input('Digite seu peso em quilos:')
Altura=input('Digite sua altura em metros:')

IMC= (Peso)/((Altura)**2)

if IMC<20:
    print('ABAIXO')

elif 20<=IMC<=25:
    print('NORMAL')
    
elif 25<IMC<=30:
    print('SOBREPESO')
    
elif 30<IMC<=40:
    print('OBESIDADE')
    
elif IMC>40:
    print('OBESIDADE GRAVE')