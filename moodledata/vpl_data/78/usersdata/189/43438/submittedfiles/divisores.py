# -*- coding: utf-8 -*-
import math
n=int(input('digite n:'))
a=int(input('digite a:'))
b=int(input('digite b:'))

cont=0
i=1
while cont<n:
    if i%a==0 and i%b==0:
        a=a//2
        b=b//2
        print(i)
        cont=cont+1
    i=i+1
