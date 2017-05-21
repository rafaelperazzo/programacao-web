ū# -*- coding: utf-8 -*-
n=int(input('digite n: '))
i=0
soma=0
while n>0:
    m=n%10
    soma=soma+m*2**i
    n=n//10
    i=i+1
print(soma)

