# -*- coding: utf-8 -*-
import math
n=int(input('digite o valor de multiplos n:'))
a=int(input('digite o valor de a:'))
b=int(input('digite o valor de b:'))
i=1
while i<=n:
    a1=a*i
    b1=b*i
    if a1<=b1:
        print(a1)
    else:
        print(b1)
i=i+1    