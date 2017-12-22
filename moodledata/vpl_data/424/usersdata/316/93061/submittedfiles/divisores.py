# -*- coding: utf-8 -*-
import math
n=int(input('digite o numero de dividores que devem ser mostrados:'))
n1=int(input('digite um numero:'))
n2=int(input('digite um numero:'))
for x in range (n1,n+1,1):
    divisores_de_x=x
for y in range (n2,n+1,1):
    divisores_de_y=y
for z in range(divisores_de_x,divisores_de_y):
    print(z)

