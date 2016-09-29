# -*- coding: utf-8 -*-
from __future__ import division

p=input('Digite aqui o peso do individuo:')
a=input('Digite aqui a altura do individuo:')

imc=(p/(a**2))

if(imc<20):
    print('ABAIXO')

if(20<=imc<=25):
    print('NORMAL')
    
if(25<imc<=30):
    print('SOBREPESO')

if(30<imc<=40):
    print('OBESIDADE')
    
if(imc>40):
    print('OBESIDADE GRAVE')