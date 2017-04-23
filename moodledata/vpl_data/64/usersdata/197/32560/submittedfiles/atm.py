# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CODIGO AQUI
saque=int(input('Digite o valor a ser sacado:'))
a=saque//20
print('O numero de cedulas de 20 é igual a:')
b=saque%20
if b>=10:
    c=b//10
    print('o número de cédulas de 10 é igual a:')
    
