# -*- coding: utf-8 -*-
a=int(input('digite o a:'))
i=0
soma=0
while a>0:
    m=a%2
    soma=soma+(m*(10**i))
    a=a//2
    i=i+1
print(soma)
