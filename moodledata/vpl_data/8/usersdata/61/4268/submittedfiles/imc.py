# -*- coding: utf-8 -*-
from __future__ import division
P=input('Digite o peso em kilos: ')
A=input('Digite a altura em metros: ')
IMC=(P/(A*A))
if IMC<20:
    print ('ABAIXO')
if 20<=IMC>=25:
    print ('NORMAL')
if 25<IMC>=30:
    print ('SOBREPESO')
if 30<IMC>=40:
    print ('OBESIDADE')
if IMC>40:
    print ('OBESIDADE GRAVE')
