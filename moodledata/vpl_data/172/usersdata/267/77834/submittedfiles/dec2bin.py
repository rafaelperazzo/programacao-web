# -*- coding: utf-8 -*-
n=int(input('Número decimal: '))
s=0
i=0
while n>0:
    s=s+(10**i)*(n%2)
    n=n//2
    i=i+1
print(s)

