# -*- coding: utf-8 -*-
from __future__ import division
#ENTRADA
p = input('Digite seu peso em kg:')
h = input('Digite sua altura em metros:')
#PROCESSAMENTO
imc = ((p)/((h)**2))
if imc<20:
    print('Baixo')
elif imc>=20 and imc<=25:
    print('Normal')
elif imc>25 and imc<=30:
    print('Sobrepeso')
elif imc>30 and imc<=40:
    print('Obesidade')
elif imc>40:
    print('Obesidade Grave')