# -*- coding: utf-8 -*-
from __future__ import division
import math
#ENTRADA
valor=int(input('Digite o valor a ser sacado:'))
#PROCESSAMENTO
cedula20=(valor)//(20)
cedula10=((valor%20)//10)
cedula5=((valor%20)%10)//(5)
cedula2=(((valor%20)%10)%5)//(2)
cedula1=((((valor%20)%10)%5)%2)//(1)
#SAÍDA
print('%.f'%(cedula20))
print('%.f'%(cedula10))
print('%.f'%(cedula5))
print('%.f'%(cedula2))
print('%.f'%(cedula1))