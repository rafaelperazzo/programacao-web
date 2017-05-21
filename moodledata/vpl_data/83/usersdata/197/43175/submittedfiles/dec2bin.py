# -*- coding: utf-8 -*-
n=int(input('Digite o valor do número decimal:'))
soma=0
i=1
while n>0:
    resto=n%2
    soma=resto*(10**i)
    i=i-1
    n=n//2
print(soma)