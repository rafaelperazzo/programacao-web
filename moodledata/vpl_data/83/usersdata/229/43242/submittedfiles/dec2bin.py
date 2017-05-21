# -*- coding: utf-8 -*-

a=int(input('digite o numero decimal:'))
soma=0
i=0

while a>0:
    resto=a%2
    soma=soma+(10**i)*resto
    a=a//2
    i=i+1
print(soma)
