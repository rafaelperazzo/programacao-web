# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CODIGO AQUI
valor=input('Digite o valor a ser sacado:')

notas20=int(valor/20)
notas10=int((valor-notas20*20)/10)
notas5=int((valor-notas20*20-notas10*10)/5)
notas2=int((valor-notas20*20-notas10*10-notas5*5)/2)
notas1=int((valor-notas20*20-notas10*10-notas5*5-notas2*2)/1)

print(notas20)
print(notas10)
print(notas5)
print(notas2)
print(notas1)