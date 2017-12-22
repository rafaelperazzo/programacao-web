# -*- coding: utf-8 -*-
import math

n1 = int(input('Digite n1: '))
n2 = int(input('Digite n2: '))
i = 0
while True:
    i+=1
    if (n1%i)==0 and (n2%i)==0:
        if i == n1 or i==n2:
            break
    
print (i)
    




















