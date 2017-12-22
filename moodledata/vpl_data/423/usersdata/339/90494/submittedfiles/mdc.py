# -*- coding: utf-8 -*-
import math

n1=int(input('n1: '))
n2=int(input('n2: '))

for n in range(0,7,1):
    while n1%n==0:
        r1=n1//n
        n+=1
        print (r1)
    while n2%n==0:
        r2=n1//n
        n+=1
        print (r2)
    
    







