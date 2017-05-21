# -*- coding: utf-8 -*-
i=0
soma=0
n=int(input('Digite n :'))
while n>0:
    m=n%10
    soma=soma+m*2**i
    n=n//10
    i=i+1

