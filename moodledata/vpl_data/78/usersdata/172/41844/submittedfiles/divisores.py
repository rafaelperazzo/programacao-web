# -*- coding: utf-8 -*-
import math
n=int(input('digite n: '))
a=int(input('digite a: '))
b=int(input('digite b: '))
c=1
f=a*c
e=b*c
h=a*b
l=(f*e)/h
while c<=n:
    f=a*c
    l=(f*e)/h
    e=b*c
    c=c+1
    print(l)
   
   
    