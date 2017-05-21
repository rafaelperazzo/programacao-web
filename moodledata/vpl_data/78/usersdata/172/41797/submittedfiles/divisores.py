# -*- coding: utf-8 -*-
import math
n=int(input('digite n: '))
a=int(input('digite a: '))
b=int(input('digite b: '))
c=1
f=a*c
e=b*c
while c<=n:
    f=a*c
    e=b*c
    c=c+1
    if f==e:
        print('%d'%f)
    elif f!=e:  
        print('%d'%e)
    