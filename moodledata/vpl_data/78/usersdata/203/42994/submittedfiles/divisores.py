# -*- coding: utf-8 -*-
import math
n=int(input('digite n: '))
a=int(input('digite a: '))
b=int(input('digite b: '))
contador=0
i=1
while contador<n:
    v1=a*i
    v2=b*i
    i=i+1
    contador=contador+2
    print(v1)
    print(v2)