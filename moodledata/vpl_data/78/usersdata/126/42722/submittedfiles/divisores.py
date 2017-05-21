# -*- coding: utf-8 -*-
import math

n=int(input('digite a quantidade de multiplos a serem mostrados:'))
a=int(input('digite o numero 1:'))
b=int(input('digite o numero 2:'))

i=0

for i in range(1,10,1):
    if a%i==0 or b%i==0 or (a%i==0 and b%i==0):
        i=i+1
        d=i
        print(d)