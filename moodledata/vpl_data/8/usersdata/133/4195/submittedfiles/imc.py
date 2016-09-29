# -*- coding: utf-8 -*-
from __future__ import division
print('Programa para calcular o imc de um individuo.')
print('O cálculo do imc é dado por: imc=peso/altura²')
peso=input('Digite o valor do peso do individuo.')
altura=input('Digite o valor da altura do individou.')
imc=peso/(altura*altura)
if (imc<20):
    print('Abaixo')
else if(20<=imc<=25):
    print('Normal')
else if(25<imc<=30):
    print('Sobrepeso')
else if(30<imc<=40):
    print('Obesidade')
else:
    print('Obesidade grave')