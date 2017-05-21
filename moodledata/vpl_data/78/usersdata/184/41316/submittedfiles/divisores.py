# -*- coding: utf-8 -*-
import math
n=int(input('digite n:'))
a=int(input('digite a:'))
b=int(input('digite b:'))
contador=0
i=1
while contador<=n:
    if i%a==0 or i%b==0:
        print(i)
        contador=contador+1
    i=i+1