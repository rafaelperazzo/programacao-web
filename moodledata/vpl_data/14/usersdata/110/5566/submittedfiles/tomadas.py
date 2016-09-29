# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CODIGO AQUI
tom=int(input(' Digite número de tomadas em cada régua: '))
a=(tom//1000)-1
b=((tom%1000)//100)-1
c=(((tom%1000)%100)//10)-1
d=((tom%1000)%100)%10
total=a+b+c+d
print(total)
