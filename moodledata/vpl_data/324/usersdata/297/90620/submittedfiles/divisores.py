# -*- coding: utf-8 -*-
import math
n=int(input('digite o numero de multiplos desejado: '))
a=int(input('digite o numero desejado a: '))
b=int(input('digite o numero desejado b: '))
y=1
for i in range(0,n,1):
    t=a*y
    u=b*y
    if u==t :
        print('%d'%u)
    elif u<t :
        print('%d'%u)
        print('%d'%t)
    else :
        print('%d'%t)
        print('%d'%u)
    y=y+1