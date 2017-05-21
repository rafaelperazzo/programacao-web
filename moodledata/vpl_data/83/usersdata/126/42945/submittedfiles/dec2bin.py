# -*- coding: utf-8 -*-

n=int(input('digite um numero inteiro na base decimal:'))

i=1
soma=0
while i>0:
    resto=n%2
    n=n//2
    soma=soma+resto*(10**i)
    i=i+1
print(soma)
    