# -*- coding: utf-8 -*-
soma=0
i=0
while (n>0):
    resto=n%10
    soma=soma+resto*(2**i)
    i=i+1
    n=n//10
print(soma)
