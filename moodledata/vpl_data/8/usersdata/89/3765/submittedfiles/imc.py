# -*- coding: utf-8 -*-
from __future__ import division
#entrada
p=input('digite o valor do peso p:')
h=input('digite o valor da altura h:')
#processamento
IMC=p/(h**2)
#saida 
if IMC<20:
    print('abaixo')
if 20<=IMC<=25:
    print('normal')
if 25<IMC<=30:
    print('sobrepeso')
if 30<IMC<=40:
    print('obesidade')
if IMC>40:
    print('obesidade grave')
    

