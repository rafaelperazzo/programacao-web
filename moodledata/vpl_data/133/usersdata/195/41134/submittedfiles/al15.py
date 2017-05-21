# -*- coding: utf-8 -*-
for n in range (1000,10000,1):
    n1=n//100
    n2=n%100
    if n**(1/2)==n1+n2:
        print(n)