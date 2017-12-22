# -*- coding: utf-8 -*-
import math
n=int(input('digite o numero de multiplos que devem ser mostrados:'))
n1=int(input('digite um numero:'))
n2=int(input('digite um numero:'))
for x in range (n1,n+1,1):
    while (x%n)==0:
        for z in range (n):
            z=x%n
            z=z+n
        print(z)
for y in range (n2,n+1,1):
    if (y%n)==0:
        print(y)

