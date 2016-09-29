# -*- coding: utf-8 -*-
from __future__ import division
#ENTRADA
p=input ('insira o peso em kilos:')
h=input ('insira a altura em metros:')

#PROCESSAMENTO
imc=(p)/(h**2)

#SAIDA
if imc=<20:
    print ('abaixo')
if 20<=imc<=25:
    print ('normal')
if 25<=imc<=30:
    print ('sobrepeso')
if 30<=imc<=40:
    print ('obesidade')
if imc>=40:
    print ('obesidade grave')
