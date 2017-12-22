# -*- coding: utf-8 -*-
import math
n=int(input('digite o numero de multiplos desejado: '))
a=int(input('digite o numero desejado a: '))
b=int(input('digite o numero desejado b: '))
cont=0
y=1
z=1
t=a*y
u=b*z
while cont<n :
    while t<u :
        if cont<n :
            print('%d'%t)
            cont=cont+1
            y=y+1
            t=a*y
    if cont<n :
        u=b*z
        print('%d'%u)
        z=z+1
    cont=cont+1