# -*- coding: utf-8 -*-
import math
a=int(input('digite a:'))
b=int(input('digite b:'))
cont=0
if a>b:
    for i in range(a,a-1,1):
        if (a%i)==0 and (b%i==0):
            mdc=i
    cont=cont+1
if b>a:
    for i in range(a,b-1,1):
        if (a%i)==0 and (b%i==0):
            mdc=i
    cont=cont+1
print(cont)
