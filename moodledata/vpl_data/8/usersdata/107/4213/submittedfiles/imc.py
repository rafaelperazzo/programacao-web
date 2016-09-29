# -*- coding: utf-8 -*-
from __future__ import division
peso=input('digite o seu peso:')
altura=input('digite sua altura:')
imc=peso/(altura**2)
if imc<20:
    print('BAIXO')
elif 20<=imc<=25:
    print('NORMAL')
if 25<imc<=30:
    print('SOBREPESO')
elif 30<imc<=40:
    print('OBESIDADE')
if imc>40:
    print('OBESIDADE GRAVE')
