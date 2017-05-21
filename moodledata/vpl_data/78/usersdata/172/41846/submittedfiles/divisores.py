# -*- coding: utf-8 -*-
import math
n=int(input('digite n: '))
a=int(input('digite a: '))
b=int(input('digite b: '))
i=1
c=0
while i<=n and c<=n:
    ma=a*i
    mb=b*i
    i=i+1
    if ma=mb:
        print(ma)
        c=c+1
    elif ma>mb:
        print(ma)
        print(mb)
        c=c+2
    else:
        print(mb)
        print(ma)
        c=c+2
        
    