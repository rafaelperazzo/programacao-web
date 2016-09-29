# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CODIGO AQUI
t1=input('T um: ')
t2=input('T dois: ')
t3=input('T três: ')
t4=input('T quarto: ')
g=(t1-1)+(t2-1)+(t3-1)+(t4)
print(g)





tom=input(' Digite número de tomadas em cada régua: ')
a=(tom//1000)-1
b=((tom%1000)//100)-1
c=(((tom%1000)%100)//10)-1
d=((tom%1000)%100)%10
total=a+b+c+d
print(total)
