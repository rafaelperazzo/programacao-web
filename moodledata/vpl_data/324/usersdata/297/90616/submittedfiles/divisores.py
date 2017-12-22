# -*- coding: utf-8 -*-
import math
n=int(input('digite o numero de multiplos desejado: '))
a=int(input('digite o numero desejado a: '))
b=int(input('digite o numero desejado b: '))
y=0
for i in range(0,n+1,1):
    t=a*y
    print('%d'%t)
    u=b*y
    print('%d'%u)
    y=y+1