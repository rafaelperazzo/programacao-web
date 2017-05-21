# -*- coding: utf-8 -*-
import math
n=int(input("Digite n:"))
i=1
S=0
while i<=n:
    o = i/(i*i)
    if i%2 != 0:
        S=S+o
    elif i%2 == 0:
        S=S-o
    i=i+1
print(S)
        
