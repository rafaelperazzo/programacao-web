# -*- coding: utf-8 -*-
import math
n=int(input('digite n:'))
a=int(input('digite a:'))
b=int(input('digite b:'))
mult=1
contador=0
while contador<n:
    if mult%a==0 or mult%b==0:
        print(mult)
        contador=contador+1
    mult=mult+1

