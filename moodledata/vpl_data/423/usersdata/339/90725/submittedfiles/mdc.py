# -*- coding: utf-8 -*-
import math

n1=int(input('n1: '))
n2=int(input('n2: '))

i= n1+n2

while True:
    i-=1
    if n1%i==0 and n2%i==0:
        break
print (i)


        



