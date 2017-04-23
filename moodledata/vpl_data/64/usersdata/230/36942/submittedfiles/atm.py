# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CODIGO AQUI
V = float(input('Qual valor deseja sacar? '))
n1=V//20
print(n1)
n2=(V%20)//10
print(n2)
n3=((V%20)%10)//5
print(n3)
n4=(((V%20)%10)%5)//2
print(n4)
n5=((((V%20)%10)%5)%2)//1
print(n5)