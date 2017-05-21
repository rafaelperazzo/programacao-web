# -*- coding: utf-8 -*-
n=float(input('digite n: '))
n=int(n)
exp=0
soma=0
while n>0:
    r=n%2
    soma=soma+r*10**exp
    n=n//2
    exp=exp+1
print(soma)