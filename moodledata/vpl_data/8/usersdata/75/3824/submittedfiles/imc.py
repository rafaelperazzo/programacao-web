# -*- coding: utf-8 -*-
from __future__ import division

#Entrada 

p= input ('Digite o valor de seu peso:')
h= input ('Digite o valor da sua altura:')

#Processamento e Saida

imc=p/(h**2)

if (imc<20):
    print ('Abaixo')
if (c<=30):
    print ('Normal')
if (25<imc<30):
    print ('Sobrepeso')
if (30<imc<40):
    print  ('Obesidade')
if (imc>40):
    print('Obesidade Grave')