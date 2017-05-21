# -*- coding: utf-8 -*-
n=int(input('digite o numero:'))
i=0
soma=0
while n >0:
    m=n%2
    f=(m*(10**i))
    soma=soma+f
    n=n//2
    i=i+1