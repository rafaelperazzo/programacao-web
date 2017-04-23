# -*- coding: utf-8 -*-
import math
n=int(input('digite n: '))
num=1
den=n
S=num/den
while n>0:
    S=S+(num/den)
print(S)