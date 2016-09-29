# -*- coding: utf-8 -*-
from __future__ import division
Peso=input('Digite o valor do Peso:')
Altura=input('Digita o valor da Altura:')

IMC= Peso/(Altura**2)
if IMC<20:
    print('Baixo')
elif 20<=IMC<=25:
    print('Normal')
elif 25<IMC<=30:
    print('Sobrepeso')
elif 30<IMC<=40:
    print('Obesidade')
else:
    print('Obesidade Grave')