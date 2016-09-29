# -*- coding: utf-8 -*-
from __future__ import division
#entrada
P=input('digite o valor do peso:')
A=input('digite o valor da altura:')

#processamento
imc=(P/(A**2)

if imc <20:
    print('abaixo do peso')

if 20<=imc<=25:
    print('normal')
    
if 25<imc<=30:
    print('soprepeso')
    
if 30<imc<=40:
    print('obesidade')
    
if imc>40:
    print('obesidade grave')