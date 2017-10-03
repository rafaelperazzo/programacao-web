# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CODIGO AQUI
a=int(input("Digite um valor inteiro: "))
v=(a//20)
d=((a-(v*20))//10)
c=((a-(v*20)-(d*10))//5)
d2=((a-(v*20)-(d*10)-(c*5))//2)
u=((a-(v*20)-(d*10)-(c*5)-(d2*2))//1)

print(v)
print(d)
print(c)
print(d)
print(u)
    
