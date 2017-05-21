# -*- coding: utf-8 -*-
import math

n=int(input('digite a quantidade de multiplos a serem mostrados:'))
a=int(input('digite o numero 1:'))
b=int(input('digite o numero 2:'))

i=1

for i in range(2,10,1):
    if a%i==0 or b%i==0 or (a%i==0 and b%i==0):
        d=i
        i=i+1
        print(d)