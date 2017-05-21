# -*- coding: utf-8 -*-
n=int(input('digite n:'))
i=0
soma=0
while n>0:
    c=n%10
    soma=soma*2**i
    n=n//10
    i=i+1


