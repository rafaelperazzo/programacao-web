# -*- coding: utf-8 -*-

n=int(input('digite um numero inteiro na base decimal:'))

i=1

while i>0:
    i=n//2
    resto=n%2
    n=i
    print(resto)
    