# -*- coding: utf-8 -*-
n=float(input('digite n:'))
n=int(n)
i=0
soma=0
while n>0:
    m=n%2
    soma=soma+m*10**1
    n=n//2
print(soma)

