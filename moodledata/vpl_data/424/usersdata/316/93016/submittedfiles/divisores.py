# -*- coding: utf-8 -*-
import math
n=int(input('digite o numero de dividores que devem ser mostrados:'))
n1=int(input('digite um numero:'))
n2=int(input('digite um numero:'))
for x in range (n1,n+1,1):
    x=[n1:x]
for y in range (n2,n+1,1):
    y=[n2:y]
z=(x+y)
print(z)

