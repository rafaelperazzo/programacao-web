# -*- coding: utf-8 -*-
import math
n=int(input('Digite o valor de n:'))
a=int(input('Digite o valor de c:'))
b=int(input('Digite o valor de b:'))
c=0
m=1
while c<n:
    if m%a==0 or m%b==0:
        print(m)
        c=c+1
    m=m+1
