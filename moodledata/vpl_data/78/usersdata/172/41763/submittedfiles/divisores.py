# -*- coding: utf-8 -*-
import math
n=int(input('digite n: '))
a=int(input('digite a: '))
b=int(input('digite b: '))
c=1
d=a
e=b
f=d%b
while c<=n:
    d=e
    e=f
    f=d%b
    c=c+1
    print('%d'%e)