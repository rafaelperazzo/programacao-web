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
elif 20<=IMC<=25:
    print('normal')
elif 25<IMC<=30:
    print('sobrepeso')
elif 30<IMC<=40:
    print('obesidade')
else: IMC>40:
    print('obesidade grave')
    

