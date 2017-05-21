# -*- coding: utf-8 -*-
import math
x=int(input('digite x:'))
y=int(input('digite y:'))
if x<=y:
    n=x
else:
    n=y
cont=0
while cont!=1:
    if (x%n)==0 and (y%n)==(x%n):
        cont=1
        mdc=n
    else:
        n=n-1
print(n)