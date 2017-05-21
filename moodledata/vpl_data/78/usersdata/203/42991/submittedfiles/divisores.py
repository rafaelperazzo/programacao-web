# -*- coding: utf-8 -*-
import math
n=int(input('digite n: '))
a=int(input('digite a: '))
b=int(input('digite b: '))
contador=0
i=1
while contador<n:
    a=a+a*i
    b=b+b*i
    i=i+1
    contador=contador+2
    print(a)
    print(b)