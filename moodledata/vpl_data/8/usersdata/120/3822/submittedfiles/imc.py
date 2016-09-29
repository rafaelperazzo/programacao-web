# -*- coding: utf-8 -*-
from __future__ import division
#ENTRADA
p=input('insira o peso em kilos:')
a=input('insira a altura em metros:')
#PROCESSAMENTO
imc=p/a**2
#SAIDA
if imc<20:
    print('ABAIXO')
if 20<imc<=25:
    print('NORMAL')
if 25<imc<=30:
    print('SOBREPESO')
if 30<imc<=40:
    print('OBESIDADE')
if imc>40:
    print('OBESIDADE GRAVE')
    

