# -*- coding: utf-8 -*-
from __future__ import division
peso=input('digite seu peso em kilos:')
altura=input('digite sua altura em metros:')

imc=peso/(altura**2)

if imc<20:
    print('abaixo')
if 20<=imc<=25:
    print('normal')
if 25<imc<=30:
    print('sobrepeso')
if 30<imc<=40:
    print('obesidade')
if imc>40:
    print('obesidade grave')
