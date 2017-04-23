# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CODIGO AQUI
V = float(input('Qual valor deseja sacar? '))
notas20=V//20
print(notas20)
notas10=(V%20)//10
print(notas10)
notas5=((V%20)%10)//5
print(notas5)
notas2=(((V%20)%10)%5)//2
print(notas2)
notas1=((((V%20)%10)%5)%2)//1
print(notas1)