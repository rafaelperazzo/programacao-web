# -*- coding: utf-8 -*-
import math
n=int(input('digite n: '))
a=int(input('digite a: '))
b=int(input('digite b: '))
i=1
c=0
ma=a*i
mb=b*i
if ma==mb:
    while i<=n and c<=n:
        i=i+1
        c=c+1
        print(ma)
elif ma<mb:
     while i<=n and c<=n:
        i=i+1
        c=c+2
        print(ma)
        print(mb)
else:
     while i<=n and c<=n:
        i=i+1
        c=c+2
        print(mb)
        print(ma)
        
    