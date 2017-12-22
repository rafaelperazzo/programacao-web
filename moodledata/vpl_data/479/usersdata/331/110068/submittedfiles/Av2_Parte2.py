# -*- coding: utf-8 -*-
import math
a = int(input('difgite o primeiro numero:'))
b = int(input('digite o segundo numero:'))
n = 1
for i in range (1,a,2):
    while a%n==0:
        n+=1
    else:
        n-=1
        print (n)
        break
for i in range (1,b,2):
    if a%n==0:
        n+=1
    else:
        n-=1
        print (n)
        break