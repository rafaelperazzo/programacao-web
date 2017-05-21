# -*- coding: utf-8 -*-
n=int(input('digite um valor'))
i=0
soma=0
while n>0:
    resto=n%2
    soma=soma+(resto*(10**i))
    n=n//2
    i=i+1
print(soma)    

