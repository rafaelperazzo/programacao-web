# -*- coding: utf-8 -*-
from __future__ import division
#ENTRADA
p=input('Digite o valor do seu peso:')
h=input('Digite o valor da sua altura:')
#PROCESSAMENTO
imc=(p)/(h**2)
#SAÍDA
if imc<20.00:
    print('ABAIXO')
elif imc<=25.00 and imc>=20.00:
    print('NORMAL')
elif imc>25.00 and imc<=30.00:
    print('SOBREPESO')
elif imc>30.00 and imc<=40.00:
    print('OBESIDADE')
else:
    print('OBESIDADE GRAVE')
    
    
