# -*- coding: utf-8 -*-
import math

n=int(input('Número de múltiplos: '))
a=int(input('Número 1: '))
b=int(input('Número 2: '))
i=1
while i<=n:
    if i%a==0 or i%b==0:
        print (i)
    i=i+1