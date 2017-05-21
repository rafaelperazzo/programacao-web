# -*- coding: utf-8 -*-
n=1000
while n<10000:
    pd=n%100
    sd=n//100
    soma=pd=sd
    if (n**(1/2))==soma:
        print(n)
    n=n+1