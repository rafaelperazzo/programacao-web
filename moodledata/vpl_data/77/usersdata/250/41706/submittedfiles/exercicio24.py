# -*- coding: utf-8 -*-
import math
n1=int(input('digite n1:'))
n2=int(input('digite n2:'))
i=1
d=1
while n1%i==0 and n2%d==0:
    if i==d:
        print('%d'%i)
    i=i+1
    d=d+1
    

