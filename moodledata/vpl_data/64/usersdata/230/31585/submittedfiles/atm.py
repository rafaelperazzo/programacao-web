# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CODIGO AQUI
V = float(input('Qual valor deseja sacar?'))
notas20=V//20
notas10=(V//20)%10
notas5=((V//20)//10)%5
notas2=(((V//20)//10)//5)%2
notas1=((((V//20)//10)//5)//2)%1
print(notas20)
print(notas10)
print(notas5)
print(notas2)
print(notas1)