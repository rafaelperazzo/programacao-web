# -*- coding: utf-8 -*-
n=int(input("digite um numero:"))
i=0
zoma=0
while n>0:
    m=n%2
    f=m*(10**i)
    zoma=zoma+f
    n=n//2
    i=i+1
print(zoma)

