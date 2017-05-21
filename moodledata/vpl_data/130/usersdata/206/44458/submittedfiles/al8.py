# -*- coding: utf-8 -*-

n=int(input('Digite um numero inteiro positivo:'))

i=1
while n>0:
    if n//i:
        print(n)
    i=i*n
    n=n-1
print(n)