# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CODIGO AQUI
#Entrada
a=int(input('Valor a ser sacado'))

#Processamento
nota20=a//20
b=a-(nota20*20)
nota10=b//10
c=b-(nota10*10)
nota5=c//5
d=c-(nota5*5)
nota2=d//2
e=d-(nota2*2)
nota1=e

#Saida
print(nota20)
print(nota10)
print(nota5)
print(nota2)
print(nota1)