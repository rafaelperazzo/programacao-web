# -*- coding: utf-8 -*-
import math
n=int(input('digite o numero de multiplos desejado: '))
a=int(input('digite o numero desejado a: '))
b=int(input('digite o numero desejado b: '))
y=0
cont=0
while cont<n :
    y=y+1
    t=a*y
    u=b*y
    while t<u :
        if cont<n :
            print('%d'%t)
            cont=cont+1
    if cont<n :
    print('%d'%u)
    cont=cont+1