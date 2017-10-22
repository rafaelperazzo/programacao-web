# -*- coding: utf-8 -*-
import math

x=int(input('digite o valor: '))
y=int(input('digite o valor: '))

for n in range(1,x+1,1):
    if(x%n==0):
        a=n
for n in range(1,y+1,1):
    if(y%n==0):
        b=n
        print(a)
        print('\n')
        print(b)



