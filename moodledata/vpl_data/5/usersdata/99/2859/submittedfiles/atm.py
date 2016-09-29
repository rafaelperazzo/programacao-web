# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CODIGO AQUI
valor=input('Valor: ')

notas20=(valor//20)
notas10=((valor -  notas20*20)//10)
notas5=((valor -  notas20*20 - notas10*10)//5)
notas2=((valor -  notas20*20 - notas10*10 - notas5*5)//2)
notas1=((valor -  notas20*20 - notas10*10 - notas5*5 - notas2*2)//5)

print('%.0f'%notas20)
print('%.0f'%notas10)
print('%.0f'%notas5)
print('%.0f'%notas2)
print('%.0f'%notas1)
