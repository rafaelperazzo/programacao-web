# -*- coding: utf-8 -*-
n = int(input())
i = 0
j = 1
s = 0.0
if n<0:
    n = n * (-1)

while j != n:
    s = s + (j/(n-i))
    i = i + 1
    j = j + 1
    
print("%.5f" , %s)    


import math


