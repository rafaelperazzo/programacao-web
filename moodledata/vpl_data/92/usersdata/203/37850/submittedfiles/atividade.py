# -*- coding: utf-8 -*-
import math
n=int(input('digite n: '))
num=1
den=n
S=num/den
while den>0:
    num=num+1
    den=den-1
    S=S+(num/den)
print(S)