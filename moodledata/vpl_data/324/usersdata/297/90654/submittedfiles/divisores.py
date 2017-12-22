# -*- coding: utf-8 -*-
import math
n=int(input('digite o numero de multiplos que deseja obter: '))
a=int(input('digite o numero que deseja: '))
b=int(input('digite o numero que deseja: '))
cont=0
y=1
z=1
while cont<n+1 :
    t=a*y
    u=b*z
    while t<u :
        if cont<n+1 :
            print('%d'%t)
            y=y+1
            t=a*y
            cont=cont+1
    if cont<n=1 :
        if u!=t :
            print('%d'%u)
        z=z+1
        cont=cont+1