# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CODIGO AQUI
#ENTRADA
a=int(input("valor a ser sacado: "))
#PROCESSAMENTO
nota20=a//20
q=a-(nota20*20)
nota10=q//10
w=q-(nota10*10)
nota5=w//5
e=w-(nota5*5)
nota2=e//2
r=e-(nota2*2)
nota1=r
#SAIDA
print(nota20)
print(nota10)
print(nota5)
print(nota2)
print(nota1)