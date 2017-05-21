# -*- coding: utf-8 -*-
import math
n=int(input('digite n: '))
a=int(input('digite a: '))
b=int(input('digite b: '))
cont=0
mult=1
while cont<n:
    if mult%a==0 or mult%b==0:
        print(mult)
        cont=cont+1
    mult=mult+1