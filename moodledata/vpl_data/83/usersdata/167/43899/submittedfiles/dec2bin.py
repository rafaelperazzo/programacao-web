# -*- coding: utf-8 -*-
n=int(input('digite n:'))
i=0
soma=0
while n>0:
    c=n%2
    soma=soma+c*10**i
    n=n//2
    i=i+1
print(soma)

