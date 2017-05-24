# -*- coding: utf-8 -*-
import math
a=int(input('digite a: '))
b=int(input('digite b: '))
cont=0
temp=1
if a>b:
    while temp>0:
        temp=a%b
        cont=cont+1
        a=b
        b=temp
    print(a)
    print(cont)
else:
    while temp>0:
        temp=b%a
        cont=cont+1
        b=a
        a=temp
    print(b)
    print(cont)