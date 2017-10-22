# -*- coding: utf-8 -*-
n = int(input('valor de n:'))
i = 0
j = 1
s = 0.0
if n<0:
    n = n * (-1)
    

while j != n + 1:
    s = s + (j/(n-i))
    i = i + 1
    j = j + 1
    
print("%.5f"  %s)    


import math


