# -*- coding: utf-8 -*-
import math
n=int(input('digite n: '))
a=int(input('digite a: '))
b=int(input('digite b: '))
i=1
c=1
ma=a*i
mb=(b*i)-((a*b)*i)
while i<=n and c<=n:
    ma=a*i
    i=i+1
    c=c+1
    print(ma)
while i<=n and c<=n:
    mb=(b*i)-((a*b)*i)
    i=i+1
    c=c+1
    print(mb)
    