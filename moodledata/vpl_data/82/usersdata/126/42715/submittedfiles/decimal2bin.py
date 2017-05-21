# -*- coding: utf-8 -*-

n=int(input('digite um numero inteiro na base binaria:'))
i=0
soma=0
while n>0:
    resto=n%10
    soma=resto*(2**i)
    i=i+1
print(soma)
