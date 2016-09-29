# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CODIGO AQUI
x = int(input('Digite um numero de quatro dígitos:'))

T1 =(x//1000)-1
T2 =((x%1000)//100)-1 
T3 =(((x%1000)%100)//10)-1 
T4 =((x%1000)%100)%10

N = T1+T2+T3+T4

print N