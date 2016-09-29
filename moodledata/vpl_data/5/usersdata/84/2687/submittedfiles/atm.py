# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CODIGO AQUI
v=int(input('valor a ser sacado:'))

nota20=(v//20)
nota10=(v-nota20*20)//10
nota5=(v-nota20*-nota10*10)//5
nota2=(v-nota20*20-nota10*10-nota5*5)//2
nota1=(v-nota20*20-nota10*10-nota5*5-nota2*2)

print(nota20)
print(nota10)
print(nota5)
print(nota2)
print(nota1)

