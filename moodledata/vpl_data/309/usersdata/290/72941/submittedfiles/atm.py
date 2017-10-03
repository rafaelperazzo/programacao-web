# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CODIGO AQUI
a=int(input("Digite um valor inteiro: "))
v=(a//20)
if a<(v*20):
    print(v)
    print(0)
    print(0)
    print(0)
    print(0)
d=((a-(v*20))//10)
elif a<((v*20)-(d*10)):
    print(v)
    print(d)
    print(0)
    print(0)
    print(0)
c=((a-(v*20)-(d*10))//5)
elif a<((v*20)-(d*10)-(c*5)):
    print(v)
    print(d)
    print(c)
    print(0)
    print(0)
d2=((a-(v*20)-(d*10)-(c*5))//2)
elif a<((v*20)-(d*10)-(c*5)-(d*2)):
    print(v)
    print(d)
    print(c)
    print(d)
    print(0)
u=((a-(v*20)-(d*10)-(c*5)-(d2*2))//1)
else:
    print(v)
    print(d)
    print(c)
    print(d)
    print(u)
    
