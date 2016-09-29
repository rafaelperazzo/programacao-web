# -*- coding: utf-8 -*-
from __future__ import division

#entrada
p = ('Digite o peso (em kg):')
h = ('Digite a altura (em metros):')

#processamento:
IMC = p/(h**2)

if IMC <= 20:
    print ('Abaixo')
elif IMC>20 and IMC<=25:
    print ('Normal')
elif IMC>25 and IMC<=30:
    print ('Sobrepeso')
elif IMC>30 and IMC<=40:
    print ('Obesidade')
elif IMC>40:
    print ('Obesidade grave')