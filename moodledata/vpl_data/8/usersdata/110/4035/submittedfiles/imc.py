# -*- coding: utf-8 -*-
from __future__ import division
p=input('Digite o seu peso: ')
h=input('Digite a sua altura: ')
imc=p/(h**2)
if imc<20 :
    print('Abaixo do peso')
if 20<=imc<=25:
    print('Peso normal')
if 25<imc<=30:
    print(' Sobrepeso ')
elif 30<imc<=40 :
    print('Obesidade')
if imc>40 :
    print('Obesidade grave')
