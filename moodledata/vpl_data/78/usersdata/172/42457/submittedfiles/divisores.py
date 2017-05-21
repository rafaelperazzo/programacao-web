# -*- coding: utf-8 -*-
import math
n=int(input('digite n: '))
a=int(input('digite a: '))
b=int(input('digite b: '))
i=1
c=1
ma=a*i
mb=(b*i)-(a*b)
while i<=n and c<=n:
    ma=a*i
    mb=(b*i)-(a*b)
    i=i+1
    c=c+1
    print(ma)
    print(mb)
