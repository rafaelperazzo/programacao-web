# -*- coding: utf-8 -*-
import math
n=int(input('digite n: '))
a=int(input('digite a: '))
b=int(input('digite b: '))
i=0
c=0
while i<n:
    if i%a==0 or i%b==0:
        print(i)
        c=c+1
        i=i+1
        
    