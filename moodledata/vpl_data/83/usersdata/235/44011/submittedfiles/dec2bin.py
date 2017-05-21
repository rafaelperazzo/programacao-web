# -*- coding: utf-8 -*-
n=int(input('digite o numero:'))
i=0
s=0
while n>0:
    M=n%2
    F=(M*(10**i))
    s=s+F
    n=n//2
    i=i+1
print(s)

