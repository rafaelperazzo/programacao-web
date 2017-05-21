# -*- coding: utf-8 -*-
n=1000
while n < 10000:
    pd=n%100
    sd=n//100
    soma=(pd+sd)
    raiz=(n**(1/2))
    if raiz==soma:
        print (n)
    n=n+1    