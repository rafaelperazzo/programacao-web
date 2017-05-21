# -*- coding: utf-8 -*-
import math

n=int(input('digite a quantidade de multiplos a serem mostrados:'))
a=int(input('digite o numero 1:'))
b=int(input('digite o numero 2:'))

i=0

for i in range(2,10,1):
    if i%a==0 or i%b==0:
        d=i
        print(d)