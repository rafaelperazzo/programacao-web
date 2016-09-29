# -*- coding: utf-8 -*-
from __future__ import division

alt= input('informe sua altura em metros: ')
peso= input('informe seu peso em kilos: ')

IMC=(peso)/(alt)**2

if IMC<20:
   print ('ABAIXO')
if 20<=IMC<=25:
    print ('NORMAL')
if 25<IMC<=30:
    print ('SOBREPESO')
if 30<IMC<=40:
    print ('OBESIDADE')
if IMC>40:
    print ('OBESIDADE GRAVE')
