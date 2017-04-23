# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CODIGO AQUI
V=float(input('Qual valor deseja sacar? '))
n1=V//20
n2=(V%20)//10
n3=((V%20)%10)//5
n4=(((V%20)%10)%5)//2
n5=((((V%20)%10)%5)%2)//1
print('%.1d' n1)
print('%.1d' n2)
print('%.1d' n3)
print('%.1d' n4)
print('%.1d' n5)