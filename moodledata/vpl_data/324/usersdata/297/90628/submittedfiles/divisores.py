# -*- coding: utf-8 -*-
import math
n=int(input('digite o numero de multiplos desejado: '))
a=int(input('digite o numero desejado a: '))
b=int(input('digite o numero desejado b: '))
y=1
print(1)
for i in range(1,n,1):
    t=a*y
    u=b*y
    y=y+1
    if t<u :
        print('%d'%t)
        print('%d'%u)
    elif t==u :
        print('%d'%t)
    else :
        print('%d'%u)
        print('%d'%t)