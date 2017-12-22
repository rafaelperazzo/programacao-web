# -*- coding: utf-8 -*-
import math

n = int(input('digite valor de n: '))
a = int(input('digite valor de a: '))
b = int(input('digite valor de b: '))
divisores = []
a1 = 0
b1 = 0
j=0

for i in range (0,n/2,1):
    a1 = a1+a
    b1 = b1+b
    if a1>b:
        print (b1)
        print(a1)
    else:
        print(a1)
        print(b1)
    
