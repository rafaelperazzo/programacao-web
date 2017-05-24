# -*- coding: utf-8 -*-
import math
a=float(input('digite a:'))
b=float(inpt('digite b:'))
cont=0
if a>b:
    for i in range(a,a-1,1):
        if (a%i)==0 and (b%i==0):
            mdc=i
    cont=cont+1
if b>a:
    for i in range(b,b-1,1):
        if (a%i)==0 and (b%i==0):
            mdc=i
    cont=cont+1
print(cont)
