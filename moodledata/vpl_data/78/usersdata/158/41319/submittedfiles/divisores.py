# -*- coding: utf-8 -*-
import math
n=int(input('digite quantidade de dividores:'))
a=int(input('digite a:'))
b=int(input('digite b:'))
contador=0
i=1
while contador<=n:
    if i%a==0 or i%b==0:
        contador=contador+1
        print(i)
    i=i+1