# -*- coding: utf-8 -*-
n=int(input('Digite n:'))
i=0
soma=0
while n>0:
    m=n%2
    soma=soma+m*10**i
    n=n//2
    i=i+1
print(soma)

