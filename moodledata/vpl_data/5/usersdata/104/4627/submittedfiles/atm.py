# -*- coding: utf-8 -*-
from __future__ import division
import math
#ENTRADA
valor=int(input('Digite o valor a ser sacado:'))
#PROCESSAMENTO
cedula20=(valor)//(20)
cedula10=int((valor%20)//10)
cedula5=int((valor%20)%10)//(5)
cedula2=(((valor%20)%10)%5)//(2)
cedula1=((((valor%20)%10)%5)%2)//(1)
#SAÍDA
print('%.i'%(cedula20))
print('%.i'%(cedula10))
print('%.i'%(cedula5))
print('%.i'%(cedula2))
print('%.i'%(cedula1))