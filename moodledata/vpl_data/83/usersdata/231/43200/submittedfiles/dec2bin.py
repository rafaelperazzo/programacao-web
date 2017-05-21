# -*- coding: utf-8 -*-
n=int(input('digite n :'))
i=0
soma=0
while n>0:
    resto=n%2
    soma=soma+resto*(10**i)
    i=i+1
    n=n//2
print(soma)

