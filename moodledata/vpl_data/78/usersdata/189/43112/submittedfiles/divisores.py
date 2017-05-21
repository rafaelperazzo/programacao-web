# -*- coding: utf-8 -*-
import math
a=int(input('digite a:'))
n=int(input('digite n:'))
b=int(input('digite b:'))
cont=0
i=1
while cont<n:
    if a%i==0 and b%i==0:
        print(i)
        cont=cont+1
        divisor=i
    i=i+1

