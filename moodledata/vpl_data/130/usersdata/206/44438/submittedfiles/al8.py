# -*- coding: utf-8 -*-

n=int(input('Digite um numero inteiro positivo:'))

i=1
while (n//i):
    i=i*n
    n=n-1
print(i)