# -*- coding: utf-8 -*-
n=int(input('digite um número de base decimal:'))
i=0
s=0
while n>0:
    m=n%2
    s=s+m*10**i
    n=n//2
    i=i+1
    print(s)


