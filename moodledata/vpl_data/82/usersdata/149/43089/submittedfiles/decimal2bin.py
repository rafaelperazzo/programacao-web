# -*- coding: utf-8 -*-
n=int(input('digite o valor de n:'))
i=0
soma=0
while n>0:
    resto=n%10
    soma=soma+resto*(2**i)
    i=i+1
    n=n/10
print=(soma)

