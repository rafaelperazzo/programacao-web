# -*- coding: utf-8 -*-
import math

a = int(input('Insira A: '))
b = int(input('Insira B: '))

mdc = 0
d = 2
while d<= a:
    if a%d == 0 and b%d == 0:
        mdc = d
    d = d + 1
print (mdc)





'''
if a>b:
    for i in range (1,a,1)
    if a%i and b%i:
        c += 1
print (i)
'''