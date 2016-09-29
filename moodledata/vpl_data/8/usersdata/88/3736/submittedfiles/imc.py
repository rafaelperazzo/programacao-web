# -*- coding: utf-8 -*-
from __future__ import division

alt= input('informe sua altura em metros: ')
peso= input('informe seu peso em kilos: ')

imc=(peso)/(alt)**2

if imc<20:
   print ('Abaixo')
if 20<=imc<=25:
    print ('Normal')
if 25<imc<=30:
    print ('Sobrepeso')
if 30<imc<=40:
    print ('Obesidade')
if imc>40:
    print ('Obesidade Grave')
