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
cedula1=((((valor%20)%10)%5)%)//(1)
#SAÍDA
print('cedula20')
print('cedula10')
print('cedula5')
print('cedula2')
print('cedula1')