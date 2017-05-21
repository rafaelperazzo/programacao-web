# -*- coding: utf-8 -*-
n=int(input('digite n: '))
s=0
i=1
while n>0:
    m=n%2
    s=s+m*(2**i)
    n=n//2
    i=i+1
print(s)