# -*- coding: utf-8 -*-

n=int(input('digite um numero inteiro na base decimal:'))

i=1
soma=0
while i>0:
    resto=n%2
    i=n//2
    n=i
    soma=soma+resto
print(soma)
    