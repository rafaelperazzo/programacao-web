# -*- coding: utf-8 -*-
from __future__ import division

p = input ('Digite o valor do seu peso (em quilogramas):')
h = input ('Digite o valor da sua altura (em metros):')

IMC = p/(h**2)

if (IMC<20):
    print ('Abaixo')
elif ((IMC>=20) and (IMC<=25)):
    print ('Normal')
elif ((IMC>25) and (IMC<=30)):
    print ('Sobrepeso')
elif ((IMC>30) and (IMC<=40)):
    print ('Obesidade')
else:
    print ('Obesidade Grave')