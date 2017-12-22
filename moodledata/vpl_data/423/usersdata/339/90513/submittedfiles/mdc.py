# -*- coding: utf-8 -*-
import math

n1=int(input('n1: '))
n2=int(input('n2: '))

i=0

while n1%2==0 and n2%2==0: 
    i+=1
    n1 = n1/(i*2)
    n2 = n2/(i*2)
    print(n1 , n2) 
    if i==2:
        break






