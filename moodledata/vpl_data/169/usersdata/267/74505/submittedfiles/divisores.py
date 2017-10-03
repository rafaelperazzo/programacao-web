# -*- coding: utf-8 -*-
import math

n=int(input('Número de múltiplos: '))
a=int(input('Número 1: '))
b=int(input('Número 2: '))
m=0
i=1
while m<=n:
    if i%a==0 or i%b==0:
        print (i)
        m=m+1
    i=i+1