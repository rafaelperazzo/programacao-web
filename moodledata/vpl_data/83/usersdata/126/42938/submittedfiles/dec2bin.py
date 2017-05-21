# -*- coding: utf-8 -*-

n=int(input('digite um numero inteiro na base decimal:'))

i=1
resto=0
while i>0:
    resto=n%2
    i=n//2
    n=i
    
    print(resto)
    