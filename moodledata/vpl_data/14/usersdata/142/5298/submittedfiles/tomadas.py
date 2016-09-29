# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CODIGO AQUI
x = input('Digite um numero de quatro dígitos:')

T1 = x//1000
T2 =(x%1000)//100 
T3 = ((x%1000)%100)//10 
T4 = ((x%1000)%100)%10

NumeroTomadas = ((T1-1)+(T2-2)+(T3-1)+T4)

print NumeroTomadas