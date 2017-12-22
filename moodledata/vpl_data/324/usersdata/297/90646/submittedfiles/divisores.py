# -*- coding: utf-8 -*-
import math
n=int(input('digite o numero de multiplos desejado: '))
a=int(input('digite o numero desejado a: '))
b=int(input('digite o numero desejado b: '))
y=0
z=0
cont=0
while cont<n :
    y=y+1
    z=z+1
    t=a*y
    u=b*z
    while t<u :
        if cont<n :
            t=a*y
            print('%d'%t)
            cont=cont+1
            y=y+1
    u=b*z
    if cont<n :
        print('%d'%u)
        cont=cont+1