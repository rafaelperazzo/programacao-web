# -*- coding: utf-8 -*-
from __future__ import division
p = input ('digite o seu peso em quilogramas:')
a = input ('digite a seu altura em metros:')

imc = p/(a*a)

if imc<20:
    print ('ABAIXO')
if 20<=imc<=25:
    print ( 'NORMAL')
if 25<=imc<=30:
    print ('SOBREPESO')
if 30<imc<=40:
    print ('OBESIDADE')
if imc>40:
    print ('OBESIDADE GRAVE')
   

