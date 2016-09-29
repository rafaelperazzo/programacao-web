# -*- coding: utf-8 -*-
from __future__ import division

#ENTRADA:

p= input ('Digite o peso em quilos:')
a= input ('Digite a altura em metros:')

#PROCESSAMENTO:
IMC = p/(a**2)

if IMC<20: 
   print ('ABAIXO')
if 20<= IMC <=25:
    print ('NORMAL')
if 25< IMC <=30:
    print ('SOBREPESO')
if 30< IMC <= 40:
    print ('OBESIDADE')
if IMC>40:
    print ('OBESIDADE GRAVE')