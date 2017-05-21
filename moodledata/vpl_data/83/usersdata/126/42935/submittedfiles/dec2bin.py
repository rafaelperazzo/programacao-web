# -*- coding: utf-8 -*-

n=int(input('digite um numero inteiro na base decimal:'))

i=1
resto=0
while i>0:
    i=n//2
    n=i
    resto=n%2
    print(resto)
    