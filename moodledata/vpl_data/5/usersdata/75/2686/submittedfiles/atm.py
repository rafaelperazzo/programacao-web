# -*- coding: utf-8 -*-
from __future__ import division
import math

#Entrada 

valor= int(input('Digite o valor a ser sacado:'))

#Processamento 

nota20=valor//20
nota10=(valor-nota20*20)//10
nota5=(valor-nota20*20-nota10*10)//5
nota2=((valor-nota20*20-nota10*10-nota5*5)//2)
nota1=(valor-nota20*20-nota10*10-nota5*5-nota2*2)

#Saida

print (nota20)
print (nota10)
print (nota5)
print (nota2)
print (nota1)
