# -*- coding: utf-8 -*-
a=int(input('digite a:'))
soma=0
i=0
while a>0:
    m=a%10
    soma=soma+(m*(2**i))
    i=i+1
    a=a//10
print(soma)

