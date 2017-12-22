# -*- coding: utf-8 -*-
import math
n=int(input('digite o numero de multiplos desejado: '))
a=int(input('digite o numero desejado a: '))
b=int(input('digite o numero desejado b: '))
y=0
cont=0
while cont<n :
    if cont<n :
        y=y+1
        t=a*y
        print('%d'%t)
        cont=cont+1
        if cont<n :
            u=b*y
            if t!=u :
                print('%d'%u)
                cont=cont+1